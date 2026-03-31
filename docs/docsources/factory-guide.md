# Factory Guide

Audience: users who need controlled testbench variation without duplicating component code.

## Why factory matters

Factory overrides let you swap implementations (type-wide or instance-specific) at runtime.

## Common pattern

```python
uvm_factory().set_type_override_by_type(BaseSeq, StressSeq)
```

Instance-specific variant:

```python
uvm_factory().set_inst_override_by_type(BaseDriver, FaultDriver, "uvm_test_top.env.agent.driver")
```

## Usage rules

- Apply overrides before components/sequences are created.
- Use precise instance paths for deterministic behavior.
- Keep override logic in test classes, not deep components.

## Debugging override misses

- Check class inheritance and registration assumptions.
- Verify instance path spelling and hierarchy.
- Confirm creation occurs after override call.

## Related pages

- [Recipe: Factory Override Patterns](recipes-factory-overrides.md)
- [Tutorial 5](tutorial-5-advanced-test-variants.md)
