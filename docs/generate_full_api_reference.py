#!/usr/bin/env python3
"""Generate full user-facing pyuvm API reference in Markdown.

The output is written to docs/docsources/reference-full.md.
It enumerates pyuvm.__all__ symbols and prints:
- symbol type and summary
- signatures
- parameter names/types/defaults
- return types
- method-level details for classes
"""

from __future__ import annotations

import enum
import inspect
import textwrap
from pathlib import Path
from types import BuiltinFunctionType, FunctionType, MethodDescriptorType
from typing import Any, get_type_hints

import pyuvm

OUTPUT = Path(__file__).resolve().parent / "docsources" / "reference-full.md"


def _doc_summary(obj: Any) -> str:
    doc = inspect.getdoc(obj) or ""
    if not doc:
        return "No description available."
    first = doc.splitlines()[0].strip()
    return first if first else "No description available."


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


def _write_param_table(lines: list[str], sig: inspect.Signature | None, skip_first_self: bool = False) -> None:
    lines.append("| Name | Kind | Type | Default | Description |")
    lines.append("|---|---|---|---|---|")
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
        lines.append(
            f"| `{p.name}` | `{p.kind.name}` | `{_fmt_annotation(p.annotation)}` | `{_fmt_default(p)}` | Parameter. |"
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
    _write_param_table(lines, init_sig, skip_first_self=True)
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
        _write_param_table(lines, sig, skip_first_self=True)
        ret = "Any"
        if sig is not None:
            ret = _fmt_annotation(sig.return_annotation)
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
    _write_param_table(lines, sig)

    ret = "Any"
    if sig is not None:
        ret = _fmt_annotation(sig.return_annotation)
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


def generate() -> None:
    lines: list[str] = []
    lines.append("# Full User-Facing API Reference")
    lines.append("")
    lines.append("This page is auto-generated from `pyuvm.__all__` and is intended to provide a complete user-facing API listing with explicit inputs and outputs.")
    lines.append("")
    lines.append("Type legend:")
    lines.append("")
    lines.append("- `Any`: no explicit type annotation is available in the signature.")
    lines.append("- `required` default: argument has no default and must be supplied by caller.")
    lines.append("")

    exports = sorted(set(getattr(pyuvm, "__all__", [])))

    classes: list[tuple[str, Any]] = []
    functions: list[tuple[str, Any]] = []
    constants: list[tuple[str, Any]] = []

    for name in exports:
        obj = getattr(pyuvm, name, None)
        if obj is None:
            continue
        if inspect.isclass(obj):
            classes.append((name, obj))
        elif callable(obj):
            functions.append((name, obj))
        else:
            constants.append((name, obj))

    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Exported symbols in `pyuvm.__all__`: `{len(exports)}`")
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

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    generate()
