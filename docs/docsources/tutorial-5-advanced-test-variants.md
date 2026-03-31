# Tutorial 5: Advanced Test Variants

Prerequisites: [Factory Guide](factory-guide.md), [Tutorial 3](tutorial-3-sequence-composition.md)

Goal: create new test behavior using overrides and controlled negative scenarios.

UVM concept introduced: reuse through controlled variation.

Large UVM environments rely on stable reusable components and test-level variation through factory overrides, configuration, and sequence selection.

## Runnable variant pattern

```python
@pyuvm.test()
class BaseTest(uvm_test):
	def build_phase(self):
		self.env = AluEnv("env", self)

	async def run_phase(self):
		self.raise_objection()
		seq = BaseSeq("base")
		await seq.start(self.env.seqr)
		self.drop_objection()


@pyuvm.test()
class StressTest(BaseTest):
	def build_phase(self):
		uvm_factory().set_type_override_by_type(BaseSeq, StressSeq)
		super().build_phase()


@pyuvm.test(expect_fail=True)
class NegativeTest(BaseTest):
	def build_phase(self):
		ConfigDB().set(None, "*", "INJECT_FAULT", True)
		super().build_phase()
```

Code walkthrough:

`BaseTest` defines stable baseline behavior: build the shared environment and run a baseline sequence. This acts as the reusable anchor for all variants.

`StressTest` changes behavior through a factory type override, replacing `BaseSeq` with `StressSeq` without duplicating environment code. This is the preferred UVM pattern for scalable variant creation.

`NegativeTest` demonstrates controlled failure-mode testing by publishing a fault-injection flag through ConfigDB. The `expect_fail=True` marker documents intent and prevents expected negative behavior from being misclassified as accidental breakage.

Together, these classes show how to preserve one reusable architecture while expanding coverage across normal, stress, and error paths.

## Step 1: baseline test

Start from a stable test class that creates env and launches a baseline sequence.

Checkpoint: baseline passes cleanly.

## Step 2: type override variant

Override a base sequence with a stress or forked variant.

Checkpoint: same test class now exercises expanded behavior.

## Step 3: targeted negative test

Enable a fault mode through ConfigDB and assert expected failure outcome.

Checkpoint: failure is intentional and clearly reported.

## Step 4: regression structure

Group directed, stress, and negative variants into separate tests for CI.

Checkpoint: each variant has a unique purpose and deterministic pass/fail criterion.

## What you learned

- Override-driven reuse
- Negative-test discipline
- Variant orchestration for robust regressions

Module mapping:

- Factory behavior: `pyuvm._s08_factory_classes`
- Configuration database and hierarchy: `pyuvm._s13_uvm_component`
