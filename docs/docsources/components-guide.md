# Components Guide

Audience: users building reusable pyuvm testbench architecture.

UVM idea introduced: component hierarchy and separation of concerns.

In UVM, each component has one primary responsibility. This keeps large testbenches maintainable as protocol support, checking depth, and regression matrix size grow over time.

## Roles and boundaries

- `uvm_test`: scenario and top-level configuration.
- `uvm_env`: composition of reusable subsystems.
- `uvm_agent`: active/passive protocol endpoint wrapper.
- `uvm_driver`: converts sequence items into DUT interactions.
- `uvm_monitor`: observes DUT activity without driving it.
- `uvm_scoreboard`: checks expected versus observed behavior.
- `uvm_subscriber`: receives analysis transactions.

## Typical component hierarchy

```text
uvm_test_top
  env
    agent
      seqr
      driver
      monitor
    scoreboard
    coverage
```

Why this matters:

- Tests configure scenarios, not protocol details.
- Environments compose reusable verification subsystems.
- Agents encapsulate protocol-specific implementation.
- Scoreboards and subscribers centralize checking and coverage.

## Where to place logic

- Build-time object creation in `build_phase`.
- Wiring/connection in `connect_phase`.
- Timed execution in async `run_phase`.
- Final validation in `check_phase`.

## Minimal pattern

```python
class MyEnv(uvm_env):
    def build_phase(self):
        self.seqr = uvm_sequencer("seqr", self)
        self.driver = MyDriver("driver", self)
        self.monitor = MyMonitor("monitor", self)

    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)
```

  Add a minimal top-level test:

  ```python
  @pyuvm.test()
  class MySmokeTest(uvm_test):
    def build_phase(self):
      self.env = MyEnv("env", self)

    async def run_phase(self):
      self.raise_objection()
      seq = MySeq("smoke")
      await seq.start(self.env.seqr)
      self.drop_objection()
  ```

  Module mapping:

  - Hierarchy and component behavior: `pyuvm._s13_uvm_component`
  - Predefined component classes: `pyuvm._s13_predefined_component_classes`

## Anti-patterns

- Driving DUT from monitor.
- Doing port connects in `build_phase`.
- Mixing random stimulus generation into driver logic.

## Related pages

- [Phasing Guide](phasing-guide.md)
- [Sequences Guide](sequences-guide.md)
- [TLM Guide](tlm-guide.md)
