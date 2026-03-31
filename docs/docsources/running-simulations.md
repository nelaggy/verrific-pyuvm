# Running Simulations

Audience: users who want repeatable command-line execution of pyuvm tests.

## Standard cocotb Makefile pattern

A typical setup is:

```makefile
SIM ?= icarus
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/hdl/verilog/my_dut.sv
TOPLEVEL = my_dut
MODULE = testbench
include $(shell cocotb-config --makefiles)/Makefile.sim
```

Adjust `SIM`, sources, and `TOPLEVEL` for your DUT.

## Core commands

```bash
make sim
make clean
```

Simulator selection examples:

```bash
make sim SIM=icarus
make sim SIM=questa
```

## Reading the output

Look for these checkpoints:

1. cocotb startup banner
2. pyuvm test discovery and phase progression
3. scoreboard pass/fail or explicit assertions
4. cocotb regression summary

## Fast failure triage

- Import error before simulation starts:
  - pyuvm or helper modules are not on Python path.
- Test exits immediately:
  - objections may not be raised.
- Test never ends:
  - objections not dropped, or driver/sequence handshake blocked.
- Runtime connection errors:
  - incorrect TLM port/export wiring.

## Log quality tips

- Use component-local loggers (`self.logger`) with clear context.
- Keep info logs for expected flow, error logs for mismatch conditions.
- Avoid excessive per-cycle logs unless debugging.

## Where to go next

- [Phasing Guide](phasing-guide.md) for lifecycle control
- [Troubleshooting](troubleshooting.md) for deadlock and mismatch patterns
