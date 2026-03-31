# Recipe: ConfigDB Patterns

Task: pass configuration through hierarchy safely.

## Pattern 1: global test setting

```python
ConfigDB().set(None, "*", "DISABLE_COVERAGE_ERRORS", True)
```

## Pattern 2: targeted setting

```python
ConfigDB().set(None, "uvm_test_top.env.agent*", "TIMEOUT_CYCLES", 200)
```

## Pattern 3: local fetch with fallback

```python
try:
    timeout = ConfigDB().get(self, "", "TIMEOUT_CYCLES")
except Exception:
    timeout = 100
```

## Checklist

- Centralize key names as constants.
- Prefer targeted scope before global wildcard.
- Log key + component name on lookup failure.
