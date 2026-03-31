# Recipe: Coverage Check Patterns

Task: track scenario/space coverage and enforce completion criteria.

## Set-based functional coverage

```python
self.covered.add((a, b, c, d))
```

End-of-test check:

```python
assert len(self.covered) == 16, "Coverage incomplete"
```

## Tips

- Track coverage at monitor/subscriber boundary.
- Make expected cardinality explicit.
- Allow opt-out switch for exploratory tests via ConfigDB.
