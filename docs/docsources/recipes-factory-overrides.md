# Recipe: Factory Override Patterns

Task: swap implementations per test without cloning environment code.

## Global type override

```python
uvm_factory().set_type_override_by_type(BaseSeq, StressSeq)
```

## Instance override

```python
uvm_factory().set_inst_override_by_type(BaseDriver, FaultDriver, "uvm_test_top.env.agent.driver")
```

## Checklist

- Apply override before object creation.
- Verify instance path with full hierarchy names.
- Keep overrides test-local where possible.
