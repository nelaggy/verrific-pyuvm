# Getting Started

Audience: Python engineers adopting pyuvm for RTL verification.

Outcome: understand the pyuvm mental model and run a complete project structure with confidence.

## pyuvm mental model in one page

- A `uvm_test` builds an environment.
- An environment contains reusable components: sequencers, drivers, monitors, scoreboards.
- Sequences generate transaction intent.
- Drivers translate transactions into DUT activity.
- Monitors observe DUT behavior and publish observations.
- Scoreboards compare expected and observed behavior.

In Python terms: pyuvm is a component framework plus async execution model layered on cocotb.

## Phase flow you need first

Typical flow:

1. `build_phase`: create components and set configuration.
2. `connect_phase`: wire ports/exports.
3. `run_phase`: execute async stimulus and checking.
4. `check_phase` / `report_phase`: summarize and fail/pass.

For most users, mastering this subset is enough to build effective testbenches.

## Core conventions

- Keep timed behavior in async phase methods, especially `run_phase`.
- Use `raise_objection()` and `drop_objection()` to control test duration.
- Use `ConfigDB().set()` in test/env and `ConfigDB().get()` in lower components.
- Keep transactions as plain Python objects extending `uvm_sequence_item`.

## Recommended project layout

```text
project/
  testbench.py
  dut_if.py
  hdl/
    verilog/
    vhdl/
  Makefile
```

## Install and validate

```bash
pip install -e .
python -c "from pyuvm import uvm_object; print(uvm_object('ok').get_name())"
```

If this prints `ok`, your package import path is correct.

## First practical path

1. Complete [Quickstart](quickstart.md).
2. Run one of the example benches under `examples/`.
3. Read concept guides in this order:
4. [Components](components-guide.md)
5. [Phasing](phasing-guide.md)
6. [Sequences](sequences-guide.md)
7. [TLM](tlm-guide.md)
8. [ConfigDB](configdb-guide.md)

## Pitfalls for Python users new to UVM

- Forgetting that `run_phase` is concurrent across components.
- Omitting objections, causing tests to end too early or hang.
- Treating ConfigDB like a global dict without scope discipline.
- Mixing monitor responsibilities with driver responsibilities.
