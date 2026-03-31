# Recipe: Scoreboard Patterns

Task: compare expected and actual behavior robustly.

## Dual-stream command/result pattern

Use separate FIFOs for command and result streams, then compare in check/report flow.

```python
predicted = predict(cmd)
assert predicted == actual, f"expected={predicted} actual={actual} cmd={cmd}"
```

## Tips

- Include operation context in mismatch logs.
- Keep predictor function deterministic and side-effect free.
- Count compared transactions and report totals.
