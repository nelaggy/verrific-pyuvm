# Tutorial 1: Minimal Environment

Prerequisites: [Quickstart](quickstart.md)

Goal: build a compact but complete test/env/sequencer/driver flow.

UVM concept introduced: transaction-level stimulus path.

In classic UVM architecture, a sequence produces transactions, a sequencer arbitrates, and a driver performs timed interactions. This tutorial focuses on that backbone.

## Complete runnable skeleton

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
			assert item.value == 42
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

	The import section brings in pyuvm classes and the test decorator. Using explicit class-based structure from the first tutorial teaches the same architectural shape you will use in larger environments.

	`PingItem` defines transaction payload. For now it has one field, but this pattern scales to any protocol payload shape.

	`PingSeq` generates one transaction and performs the sequence handshake. The explicit `await` points are the key runtime boundaries where control moves between sequence and driver.

	`PingDriver.run_phase` blocks on `get_next_item`, validates the transaction, and calls `item_done`. If `item_done` is skipped, sequences can stall and tests can hang.

	`PingEnv` does composition and connection. The sequencer-driver connection is the backbone of transaction flow.

	`PingTest` controls lifecycle. Objections are raised before workload starts and dropped after completion to signal the phase scheduler that the test can end.

## Step 1: create item, sequence, driver

Implement one transaction item and one sequence that sends exactly one item.

Checkpoint: driver receives one item and calls `item_done()`.

## Step 2: create environment

Instantiate sequencer and driver in `build_phase`, connect in `connect_phase`.

Checkpoint: no connection errors at startup.

## Step 3: create test

Raise objection, start sequence on env sequencer, drop objection.

Checkpoint: simulation exits cleanly.

## Step 4: add one assertion

Driver asserts transaction field values.

Checkpoint: intentionally break value once to verify fail behavior, then restore.

## What you learned

- Minimal pyuvm architecture
- Handshake correctness
- Objection lifecycle

Module mapping:

- Components and hierarchy: `pyuvm._s13_uvm_component`
- Sequences and sequencers: `pyuvm._s14_15_python_sequences`
- Phasing: `pyuvm._s09_phasing`
