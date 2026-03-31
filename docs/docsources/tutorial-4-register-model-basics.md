# Tutorial 4: Register Model Basics

Prerequisites: [Core API Reference](reference-core.md), [Advanced API Reference](reference-advanced.md)

Goal: execute a practical frontdoor register write/poll/read loop with pyuvm RAL components.

UVM concept introduced: abstract register intent separated from bus protocol details.

UVM RAL lets you express verification in terms of register operations while adapters and bus sequences handle transport details.

## Runnable flow skeleton

```python
class RegFlowSeq(uvm_sequence):
	async def body(self):
		src_addr = 0x00
		cmd_addr = 0x04
		result_addr = 0x08

		src_value = (0x23 << 8) | 0x11
		await self.reg_write(src_addr, src_value)

		start_cmd = 0x01
		await self.reg_write(cmd_addr, start_cmd)

		timeout = 100
		for _ in range(timeout):
			status = await self.reg_read(cmd_addr)
			if status & 0x20:
				break
		else:
			raise RuntimeError("Timeout waiting for DONE")

		result = await self.reg_read(result_addr)
		assert result is not None
```

Code walkthrough:

`RegFlowSeq` expresses a register-driven scenario as one coherent sequence. The local address constants make the command/status/result contract explicit for readability and maintainability.

The source write programs operands or configuration into the DUT-visible register model path. The command write initiates execution.

The poll loop repeatedly reads status until a done bit is set. The timeout guard is essential in robust verification because it turns deadlocks into diagnosable failures.

The final result read and assertion closes the flow by verifying that the command path produced observable output. In full benches, this is often combined with scoreboard checks for richer diagnostics.

The `reg_write` and `reg_read` helper methods are typically implemented using a register adapter and your bus-facing driver/BFM.

## Step 1: model essentials

Create a block, register(s), and map address offsets.

Checkpoint: model builds without configuration errors.

## Step 2: adapter path

Use `uvm_reg_adapter` to convert register operations to bus operations used by your driver/bfm.

Checkpoint: register writes create expected bus transactions.

## Step 3: write command and poll status

Issue command register write, then repeatedly read status until done bit is set.

Checkpoint: loop exits and reports final status.

## Step 4: read result register

Read data register and compare with expected computation.

Checkpoint: pass/fail log includes expected and actual values.

## What you learned

- Practical frontdoor access flow
- Adapter responsibilities
- Status-driven control loops

Module mapping:

- Register model core: `pyuvm._reg.uvm_reg`, `pyuvm._reg.uvm_reg_block`
- Address maps and transactions: `pyuvm._reg.uvm_reg_map`, `pyuvm._reg.uvm_reg_item`
- Adapter/predictor: `pyuvm._reg.uvm_reg_adapter`, `pyuvm._reg.uvm_reg_predictor`
