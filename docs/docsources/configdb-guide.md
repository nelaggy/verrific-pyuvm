# ConfigDB Guide

Audience: users configuring components without hardcoded coupling.

## What ConfigDB does

`ConfigDB` lets upper layers publish values and lower layers retrieve them using scope and key.

## Basic usage

Set value from test/env:

```python
ConfigDB().set(None, "*", "SEQR", self.seqr)
```

Get value from component:

```python
self.seqr = ConfigDB().get(self, "", "SEQR")
```

## Scope and wildcard behavior

- Instance paths support wildcard matching.
- More specific matches should be preferred over broad global entries.
- Keep key names stable and explicit.

## Best practices

- Define constants for key names.
- Start with local scope, widen only when necessary.
- Log full component name when debugging misses.

## Common failures

- Typo mismatch in keys between `set` and `get`.
- Over-broad wildcard entries shadowing intended values.
- Getting too early before value is set in phase flow.

## Related pages

- [Recipe: ConfigDB Patterns](recipes-configdb-patterns.md)
- [Troubleshooting](troubleshooting.md)
