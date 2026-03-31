#!/usr/bin/env python3
"""Generate split user-facing pyuvm API reference in Markdown.

Outputs are written to docs/docsources/reference-api-*.md and reference-full.md.
The content is derived from pyuvm.__all__ and includes:
- symbol summaries
- signatures
- parameter names/types/defaults/descriptions
- return types
- method-level details for classes
"""

from __future__ import annotations

import enum
import inspect
import re
from pathlib import Path
from types import BuiltinFunctionType, FunctionType, MethodDescriptorType
from typing import Any

import pyuvm

DOCS_DIR = Path(__file__).resolve().parent / "docsources"

OUTPUTS = {
    "core": DOCS_DIR / "reference-api-core.md",
    "tlm": DOCS_DIR / "reference-api-tlm.md",
    "ral": DOCS_DIR / "reference-api-ral.md",
    "utils": DOCS_DIR / "reference-api-utils.md",
    "full": DOCS_DIR / "reference-full.md",
}

PARAM_RE = re.compile(
    r"^\s*:param\s+(?:(?P<ptype>[\w\[\], .|]+)\s+)?(?P<pname>[*]*\w+)\s*:\s*(?P<desc>.*)$"
)
RTYPE_RE = re.compile(r"^\s*:rtype:\s*(?P<rtype>.*)$")


def _doc_summary(obj: Any) -> str:
    doc = inspect.getdoc(obj) or ""
    if not doc:
        return "No description available."
    first = doc.splitlines()[0].strip()
    return first if first else "No description available."


def _parse_doc_params(obj: Any) -> tuple[dict[str, tuple[str | None, str]], str | None]:
    """Parse :param and :rtype entries from docstring.

    Returns:
        (param_map, rtype)
        param_map[name] = (type_or_none, description)
    """
    doc = inspect.getdoc(obj) or ""
    params: dict[str, tuple[str | None, str]] = {}
    rtype: str | None = None

    for line in doc.splitlines():
        m = PARAM_RE.match(line)
        if m:
            pname = m.group("pname") or ""
            ptype = m.group("ptype")
            desc = (m.group("desc") or "").strip() or "Parameter."
            params[pname.lstrip("*")] = (ptype.strip() if ptype else None, desc)
            continue

        r = RTYPE_RE.match(line)
        if r:
            rr = (r.group("rtype") or "").strip()
            if rr:
                rtype = rr

    return params, rtype


def _infer_name_type(name: str) -> str | None:
    lname = name.lower()
    if lname in {
        "name",
        "label",
        "inst_path",
        "full_inst_path",
        "parent_inst_path",
        "inst_name",
        "field_name",
        "description",
        "method_name",
        "type_name",
        "alias_type_name",
        "original_type_name",
        "override_type_name",
        "requested_type_name",
    }:
        return "str"
    if lname in {
        "replace",
        "free_handle",
        "call_pre_post",
        "keep_singletons",
        "enable",
        "disable",
        "check",
    }:
        return "bool"
    if lname in {
        "debug_level",
        "logging_level",
        "stacklevel",
        "transaction_id",
        "txn_id",
        "accept_time",
        "begin_time",
        "end_time",
        "n_bits",
        "size",
        "offset",
        "addr",
        "index",
        "timeout",
        "count",
    } or lname.endswith("_id"):
        return "int"
    if lname in {"handler"}:
        return "logging.Handler"
    if lname in {"context", "parent", "comp", "initiator"}:
        return "uvm_component"
    return None


def _infer_return_type(name: str, sig: inspect.Signature | None, doc_rtype: str | None) -> str:
    if sig is not None and sig.return_annotation is not inspect.Signature.empty:
        return _fmt_annotation(sig.return_annotation)
    if doc_rtype:
        return doc_rtype

    lname = name.lower()
    if lname.startswith(("is_", "has_", "can_", "exists_")):
        return "bool"
    if lname.startswith(("get_", "peek_", "try_get", "try_peek")):
        return "object"
    if lname.startswith(("set_", "put_", "write_", "drop_", "raise_")):
        return "None"
    return "object"


def _fmt_annotation(ann: Any) -> str:
    if ann is inspect.Signature.empty:
        return "Any"
    if isinstance(ann, type):
        return ann.__name__
    text = str(ann)
    return text.replace("typing.", "")


def _fmt_default(param: inspect.Parameter) -> str:
    if param.default is inspect.Signature.empty:
        return "required"
    return repr(param.default)


def _safe_signature(obj: Any) -> inspect.Signature | None:
    try:
        return inspect.signature(obj)
    except (TypeError, ValueError):
        return None


def _write_param_table(
    lines: list[str],
    owner: Any,
    sig: inspect.Signature | None,
    skip_first_self: bool = False,
) -> None:
    lines.append("| Name | Kind | Type | Default | Description |")
    lines.append("|---|---|---|---|---|")

    doc_params, _ = _parse_doc_params(owner)

    if sig is None:
        lines.append("| n/a | n/a | Any | n/a | Signature not available. |")
        lines.append("")
        return

    params = list(sig.parameters.values())
    if skip_first_self and params and params[0].name in {"self", "cls"}:
        params = params[1:]

    if not params:
        lines.append("| (none) | - | - | - | No input parameters. |")
        lines.append("")
        return

    for p in params:
        doc_type, doc_desc = doc_params.get(p.name, (None, "Parameter."))
        if p.annotation is not inspect.Signature.empty:
            ptype = _fmt_annotation(p.annotation)
        elif doc_type:
            ptype = doc_type
        elif p.default is not inspect.Signature.empty and p.default is not None:
            ptype = type(p.default).__name__
        elif p.kind is inspect.Parameter.VAR_POSITIONAL:
            ptype = "tuple[object, ...]"
        elif p.kind is inspect.Parameter.VAR_KEYWORD:
            ptype = "dict[str, object]"
        else:
            ptype = _infer_name_type(p.name) or "object"

        lines.append(
            f"| `{p.name}` | `{p.kind.name}` | `{ptype}` | `{_fmt_default(p)}` | {doc_desc} |"
        )
    lines.append("")


def _public_methods(cls: type) -> list[tuple[str, Any]]:
    methods: list[tuple[str, Any]] = []
    for name, member in inspect.getmembers(cls):
        if name.startswith("_"):
            continue
        if not callable(member):
            continue
        if isinstance(member, (BuiltinFunctionType, MethodDescriptorType)):
            methods.append((name, member))
            continue
        if isinstance(member, FunctionType):
            methods.append((name, member))
            continue
        if inspect.ismethod(member):
            methods.append((name, member))
    # Stable order
    methods.sort(key=lambda x: x[0])
    return methods


def _class_section(lines: list[str], name: str, cls: type) -> None:
    lines.append(f"## Class `{name}`")
    lines.append("")
    lines.append(f"Module: `{cls.__module__}`")
    lines.append("")
    lines.append(_doc_summary(cls))
    lines.append("")

    if issubclass(cls, enum.Enum):
        lines.append("### Enum Members")
        lines.append("")
        lines.append("| Name | Value | Description |")
        lines.append("|---|---|---|")
        for member in cls:
            lines.append(f"| `{member.name}` | `{member.value}` | Enum member. |")
        lines.append("")
        return

    init = getattr(cls, "__init__", None)
    init_sig = _safe_signature(init)
    lines.append("### Constructor")
    lines.append("")
    if init_sig is not None:
        lines.append(f"Signature: `{name}{init_sig}`")
    else:
        lines.append("Signature: not available")
    lines.append("")
    lines.append("Inputs")
    lines.append("")
    _write_param_table(lines, init, init_sig, skip_first_self=True)
    lines.append(f"Output: `{name}` instance")
    lines.append("")

    methods = _public_methods(cls)
    if methods:
        lines.append("### Methods")
        lines.append("")

    for method_name, method in methods:
        sig = _safe_signature(method)
        lines.append(f"#### `{name}.{method_name}`")
        lines.append("")
        lines.append(_doc_summary(method))
        lines.append("")
        if sig is not None:
            lines.append(f"Signature: `{method_name}{sig}`")
        else:
            lines.append("Signature: not available")
        lines.append("")
        lines.append("Inputs")
        lines.append("")
        _write_param_table(lines, method, sig, skip_first_self=True)
        _, doc_rtype = _parse_doc_params(method)
        ret = _infer_return_type(method_name, sig, doc_rtype)
        lines.append(f"Output: `{ret}`")
        lines.append("")


def _function_section(lines: list[str], name: str, fn: Any) -> None:
    lines.append(f"## Function `{name}`")
    lines.append("")
    lines.append(f"Module: `{fn.__module__}`")
    lines.append("")
    lines.append(_doc_summary(fn))
    lines.append("")

    sig = _safe_signature(fn)
    if sig is not None:
        lines.append(f"Signature: `{name}{sig}`")
    else:
        lines.append("Signature: not available")
    lines.append("")
    lines.append("Inputs")
    lines.append("")
    _write_param_table(lines, fn, sig)

    _, doc_rtype = _parse_doc_params(fn)
    ret = _infer_return_type(name, sig, doc_rtype)
    lines.append(f"Output: `{ret}`")
    lines.append("")


def _constant_section(lines: list[str], name: str, value: Any) -> None:
    lines.append(f"## Constant `{name}`")
    lines.append("")
    lines.append(f"Module: `{type(value).__module__}`")
    lines.append("")
    lines.append(f"Type: `{type(value).__name__}`")
    lines.append("")
    lines.append(f"Value: `{value!r}`")
    lines.append("")


def _category_for(name: str, obj: Any) -> str:
    module = getattr(obj, "__module__", "")
    lname = name.lower()

    ral_names = {
        "uvm_access_e",
        "uvm_check_e",
        "uvm_coverage_model_e",
        "uvm_door_e",
        "uvm_elem_kind_e",
        "uvm_endianness_e",
        "uvm_hier_e",
        "uvm_path_e",
        "uvm_predict_e",
        "uvm_status_e",
        "uvm_hdl_path_concat",
        "uvm_hdl_path_slice",
        "uvm_object_string_pool",
    }

    if (
        "._reg." in module
        or lname.startswith("uvm_reg")
        or lname.startswith("uvm_vreg")
        or lname.startswith("uvm_mem")
        or lname in ral_names
    ):
        return "ral"

    tlm_prefixes = (
        "uvm_tlm",
        "uvm_analysis",
        "uvm_blocking",
        "uvm_nonblocking",
        "uvm_put",
        "uvm_get",
        "uvm_peek",
        "uvm_master",
        "uvm_slave",
        "uvm_transport",
        "uvm_port_base",
        "uvm_export_base",
    )
    if "_s12_uvm_tlm_interfaces" in module or lname.startswith(tlm_prefixes):
        return "tlm"

    util_names = {
        "count_bits",
        "singleton",
        "factorydata",
        "factorymeta",
        "override",
        "objection",
        "objectionhandler",
        "uvmqueue",
        "uvm_void",
        "test",
        "fifo_debug",
        "pyuvm_debug",
        "__version__",
        "uvm_root_singleton",
    }
    if module.endswith("_utility_classes") or module.endswith("_error_classes") or module.endswith("_extension_classes"):
        return "utils"
    if lname in util_names:
        return "utils"

    if lname.startswith("uvm") and ("error" in lname or lname in {"usepythonmethod", "uvmnotimplemented"}):
        return "utils"

    return "core"


def _render_page(
    title: str,
    intro: str,
    classes: list[tuple[str, Any]],
    functions: list[tuple[str, Any]],
    constants: list[tuple[str, Any]],
) -> list[str]:
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(intro)
    lines.append("")
    lines.append("Type legend:")
    lines.append("")
    lines.append("- `object`: no explicit annotation was available; type inferred from docs/defaults/name where possible.")
    lines.append("- `required` default: argument has no default and must be supplied by caller.")
    lines.append("")

    total = len(classes) + len(functions) + len(constants)
    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Symbols in this page: `{total}`")
    lines.append(f"- Classes: `{len(classes)}`")
    lines.append(f"- Functions/callables: `{len(functions)}`")
    lines.append(f"- Constants/other values: `{len(constants)}`")
    lines.append("")

    lines.append("## Index")
    lines.append("")
    lines.append("### Classes")
    lines.append("")
    for name, _ in classes:
        lines.append(f"- `{name}`")
    lines.append("")
    lines.append("### Functions")
    lines.append("")
    for name, _ in functions:
        lines.append(f"- `{name}`")
    lines.append("")
    if constants:
        lines.append("### Constants")
        lines.append("")
        for name, _ in constants:
            lines.append(f"- `{name}`")
        lines.append("")

    for name, cls in classes:
        _class_section(lines, name, cls)

    for name, fn in functions:
        _function_section(lines, name, fn)

    for name, value in constants:
        _constant_section(lines, name, value)

    return lines


def generate() -> None:
    exports = sorted(set(getattr(pyuvm, "__all__", [])))

    categorized: dict[str, dict[str, list[tuple[str, Any]]]] = {
        "core": {"classes": [], "functions": [], "constants": []},
        "tlm": {"classes": [], "functions": [], "constants": []},
        "ral": {"classes": [], "functions": [], "constants": []},
        "utils": {"classes": [], "functions": [], "constants": []},
    }

    all_classes: list[tuple[str, Any]] = []
    all_functions: list[tuple[str, Any]] = []
    all_constants: list[tuple[str, Any]] = []

    for name in exports:
        obj = getattr(pyuvm, name, None)
        if obj is None:
            continue

        cat = _category_for(name, obj)
        if inspect.isclass(obj):
            all_classes.append((name, obj))
            categorized[cat]["classes"].append((name, obj))
        elif callable(obj):
            all_functions.append((name, obj))
            categorized[cat]["functions"].append((name, obj))
        else:
            all_constants.append((name, obj))
            categorized[cat]["constants"].append((name, obj))

    pages = {
        "core": (
            "API Reference: Core",
            "Auto-generated API reference for core user-facing pyuvm classes and functions (components, phasing, sequences, factory, configuration, reporting).",
        ),
        "tlm": (
            "API Reference: TLM",
            "Auto-generated API reference for Transaction-Level Modeling interfaces, ports, exports, and channels.",
        ),
        "ral": (
            "API Reference: Register Layer (RAL)",
            "Auto-generated API reference for register model, fields, maps, adapters, predictors, and related enums/types.",
        ),
        "utils": (
            "API Reference: Errors and Utilities",
            "Auto-generated API reference for error classes, utility helpers, and extension-level callables/constants.",
        ),
    }

    for cat, (title, intro) in pages.items():
        lines = _render_page(
            title,
            intro,
            sorted(categorized[cat]["classes"], key=lambda x: x[0]),
            sorted(categorized[cat]["functions"], key=lambda x: x[0]),
            sorted(categorized[cat]["constants"], key=lambda x: x[0]),
        )
        OUTPUTS[cat].write_text("\n".join(lines) + "\n", encoding="utf-8")

    full_lines = _render_page(
        "Full User-Facing API Reference",
        "Auto-generated complete API reference for all symbols exported in `pyuvm.__all__`.",
        sorted(all_classes, key=lambda x: x[0]),
        sorted(all_functions, key=lambda x: x[0]),
        sorted(all_constants, key=lambda x: x[0]),
    )

    OUTPUTS["full"].write_text("\n".join(full_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate()
