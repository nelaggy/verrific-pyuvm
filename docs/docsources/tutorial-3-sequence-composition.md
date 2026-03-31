# Tutorial 3: Sequence Composition

Prerequisites: [Sequences Guide](sequences-guide.md)

Goal: build reusable sequence helpers and compose them into larger scenarios.

UVM concept introduced: scenario-level abstraction through sequence composition.

A core UVM idea is that verification scenarios should be expressed in sequences, not embedded in drivers. This improves reuse and keeps protocol implementation separate from test intent.

## Runnable composition example

```python
class OpItem(uvm_sequence_item):
	def __init__(self, name, a=0, b=0, op="ADD"):
		super().__init__(name)
		self.a = a
		self.b = b
		self.op = op


class OpSeq(uvm_sequence):
	def __init__(self, name, a, b, op):
		super().__init__(name)
		self.a = a
		self.b = b
		self.op = op

	async def body(self):
		item = OpItem(self.get_name(), self.a, self.b, self.op)
		await self.start_item(item)
		await self.finish_item(item)


async def do_add(seqr, a, b):
	seq = OpSeq("add_seq", a, b, "ADD")
	await seq.start(seqr)


class ScenarioSeq(uvm_sequence):
	async def body(self):
		seqr = ConfigDB().get(None, "", "SEQR")
		await do_add(seqr, 1, 1)
		await do_add(seqr, 2, 3)
		await do_add(seqr, 5, 8)
```

Code walkthrough:

`OpItem` defines operation payload (`a`, `b`, `op`) as a sequence item. This keeps data representation separate from protocol driving and supports reuse in multiple sequences.

`OpSeq` is a focused single-operation sequence. It captures operation parameters in the constructor and sends exactly one transaction through the sequence handshake in `body`.

`do_add` is a helper that wraps common sequence creation and start behavior. Small helpers like this reduce repeated boilerplate in scenario sequences.

`ScenarioSeq` composes multiple helper calls to describe algorithm-level intent. This is a key UVM scaling pattern: tests can launch one scenario sequence instead of manually stitching low-level operations.

## Step 1: define operation helpers

Create helper sequences or helper functions that each perform one protocol operation.

Checkpoint: each helper can run independently and return/record outcome.

## Step 2: compose scenario sequence

Build a parent sequence that chains helpers for a multi-step algorithm.

Checkpoint: parent sequence executes full scenario with expected ordering.

## Step 3: add mixed directed/random segments

Start with deterministic setup, then randomize remaining transactions.

Checkpoint: run multiple seeds and preserve core invariant checks.

## Step 4: response handling

Use transaction identifiers when multiple in-flight operations exist.

Checkpoint: no ambiguity in response matching.

## What you learned

- Sequence reuse patterns
- Scenario abstraction
- Controlled randomness integration

Module mapping:

- Sequence classes and response behavior: `pyuvm._s14_15_python_sequences`
