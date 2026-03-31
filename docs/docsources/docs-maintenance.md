# Docs Maintenance

Use this checklist whenever pyuvm behavior changes.

## Update workflow

1. Update concept guide for changed semantics.
2. Update affected quickstart/tutorial snippets.
3. Update relevant recipe pages.
4. Update curated reference pages if exported symbols changed.
5. Run docs build and link checks.
6. Regenerate full API reference from exports when public signatures change.

Full API generation command:

```bash
cd /path/to/pyuvm
export PYTHONPATH=/path/to/pyuvm
python docs/generate_full_api_reference.py
```

This command regenerates:

- `docs/docsources/reference-api-core.md`
- `docs/docsources/reference-api-tlm.md`
- `docs/docsources/reference-api-ral.md`
- `docs/docsources/reference-api-utils.md`
- `docs/docsources/reference-full.md`

## Quality gates

- No new Sphinx warnings.
- No broken links.
- No orphan pages.
- Snippets include imports and execution context.

## Ownership map

- Core architecture docs: component/phasing/sequence/TLM maintainers
- Configuration/factory docs: framework maintainers
- RAL docs: register model maintainers
- Tutorial and recipe docs: examples maintainers

## CI recommendation

Add docs checks to CI:

```bash
cd docs
make html
make linkcheck
```
