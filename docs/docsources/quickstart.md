# Quickstart: First pyuvm Testbench

Audience: Python developers who are new to pyuvm and UVM-style testbench architecture.

Goal: build and run a minimal pyuvm test that demonstrates phasing, objections, and one passing check.

Estimated time: 10-15 minutes.

## Prerequisites

- Python 3.8+ installed
- A simulator supported by cocotb (for example Icarus)
- pyuvm repository cloned locally

## 1. Install pyuvm in editable mode

```bash
cd <path-to-pyuvm>
pip install -e .
```

## 2. Create a minimal testbench file

Create a file named `testbench.py` with the following content:

```python
import pyuvm
from pyuvm import *


class PingItem(uvm_sequence_item):
    def __init__(self, name, value=0):
        super().__init__(name)
        self.value = value


class PingSeq(uvm_sequence):
    async def body(self):
        item = PingItem("item", value=42)
        await self.start_item(item)
        await self.finish_item(item)


class PingDriver(uvm_driver):
    async def run_phase(self):
        while True:
            item = await self.seq_item_port.get_next_item()
            assert item.value == 42, f"Unexpected value: {item.value}"
            self.seq_item_port.item_done()


class PingEnv(uvm_env):
    def build_phase(self):
        self.seqr = uvm_sequencer("seqr", self)
        self.driver = PingDriver("driver", self)

    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


@pyuvm.test()
class PingTest(uvm_test):
    def build_phase(self):
        self.env = PingEnv("env", self)

    async def run_phase(self):
        self.raise_objection()
        seq = PingSeq("ping")
        await seq.start(self.env.seqr)
        self.drop_objection()
```

    Code walkthrough:

    The `PingItem` class is your transaction object. In UVM terms, this is the unit of intent that moves from sequence to driver. You keep protocol-specific fields here, not in the driver.

    `PingSeq` is the stimulus generator. The `start_item` and `finish_item` calls are the sequence side of the handshake and are intentionally explicit so you can reason about ordering and blocking points in async execution.

    `PingDriver` is where intent becomes timed behavior. In this minimal example it only checks a value and completes the handshake with `item_done`, but in real benches it would call BFM methods or drive signal-level operations.

    `PingEnv` composes sequencer and driver and wires them in `connect_phase`. This keeps structure and wiring deterministic and matches UVM lifecycle best practice.

    `PingTest` owns orchestration, raises objections to keep the test alive during activity, launches the sequence, then drops objections for clean completion.

## 3. Run the test

Run with your existing cocotb flow. In this repository, use an example makefile layout and set `MODULE=testbench`.

```bash
make sim
```

Code walkthrough:

`make sim` starts the cocotb-driven simulation flow defined by your makefile. The makefile identifies the HDL top, Python module name, and simulator backend.

During this run, pyuvm performs phase execution, component construction, port wiring, sequence execution, and final completion reporting. If the command exits successfully with no assertion failures, your minimal UVM flow is functioning.

Expected behavior:

- The test finishes cleanly.
- No assertion failures appear.
- You see pyuvm phase and completion log output in the cocotb stream.

## 4. What you just exercised

- `uvm_test` build and run phases
- Objection-based test lifetime control
- Sequence to sequencer to driver handshake
- Basic component creation and TLM connection

## Common failures

- Test hangs forever: missing `drop_objection()` or missing `item_done()`.
- Attribute error on `seqr`: sequence started before env build/connect completed.
- Connection errors: `seq_item_port.connect(seq_item_export)` not called.

## Next steps

- Continue with [Getting Started](getting-started.md)
- Learn runtime details in [Running Simulations](running-simulations.md)
- Deepen architecture understanding in [Core Concepts](concepts-index.md)
