# Reporting and Logging Guide

Audience: users who need high-signal debug output from pyuvm runs.

## Logging model

pyuvm uses Python logging through component-local `self.logger` instances.

## Practical recommendations

- Use `info` for expected flow checkpoints.
- Use `warning` for recoverable anomalies.
- Use `error` for mismatches and violations.
- Keep messages structured: include operation, inputs, expected, actual.

## Typical mismatch log

```python
self.logger.error(
    "MISMATCH op=%s a=%s b=%s expected=%s actual=%s",
    op, a, b, expected, actual,
)
```

## Debug depth control

Set logger levels to reduce noise during stable regressions and increase detail during failure triage.

## Related pages

- [Running Simulations](running-simulations.md)
- [Troubleshooting](troubleshooting.md)
