# Phasing Guide

Audience: users who need predictable lifecycle behavior and test completion control.

UVM idea introduced: deterministic lifecycle orchestration.

Without phases, testbenches often rely on ad hoc ordering assumptions. UVM phases provide explicit lifecycle boundaries so structure setup, wiring, and timed execution remain consistent across large teams.

## Common phases

1. `build_phase`: instantiate components and set config.
2. `connect_phase`: connect ports and exports.
3. `end_of_elaboration_phase`: finalize structure.
4. `start_of_simulation_phase`: final setup before runtime.
5. `run_phase`: async concurrent execution.
6. `extract_phase`, `check_phase`, `report_phase`, `final_phase`: summarize and finalize.

## Execution direction

- Build-like phases are top-down.
- Check/report-like phases are bottom-up.
- `run_phase` executes concurrently across components.

## Objections

Use objections to keep the test alive during active stimulus/checking:

```python
async def run_phase(self):
    self.raise_objection()
    await self.main_seq.start(self.env.seqr)
    self.drop_objection()
```

If objections are not dropped, tests hang. If objections are never raised, tests may finish too early.

## Recovery checklist for phase issues

- Confirm `run_phase` is async when awaited operations are used.
- Confirm every raise has a guaranteed drop path.
- Confirm long-running monitors do not block drops in test logic.

Module mapping:

- Phase definitions and scheduling: `pyuvm._s09_phasing`
- Component-level objection APIs: `pyuvm._s13_uvm_component`

## Related pages

- [Troubleshooting](troubleshooting.md)
- [Tutorial 1](tutorial-1-minimal-env.md)
