# Tutorial 2: Scoreboard and Analysis

Prerequisites: [Tutorial 1](tutorial-1-minimal-env.md), [TLM Guide](tlm-guide.md)

Goal: add monitor-driven checking with analysis ports and a scoreboard.

UVM concept introduced: passive observation and centralized checking.

In UVM, monitors observe protocol activity without driving behavior. Scoreboards compare expected and actual results, typically fed through analysis ports and FIFOs.

## Runnable monitor/scoreboard sketch

```python
class CmdMonitor(uvm_component):
	def build_phase(self):
		self.ap = uvm_analysis_port("ap", self)

	async def run_phase(self):
		while True:
			cmd = await self.bfm.get_cmd()
			self.ap.write(cmd)


class ResultMonitor(uvm_component):
	def build_phase(self):
		self.ap = uvm_analysis_port("ap", self)

	async def run_phase(self):
		while True:
			result = await self.bfm.get_result()
			self.ap.write(result)


class AluScoreboard(uvm_component):
	def build_phase(self):
		self.cmd_fifo = uvm_tlm_analysis_fifo("cmd_fifo", self)
		self.result_fifo = uvm_tlm_analysis_fifo("result_fifo", self)
		self.cmd_export = self.cmd_fifo.analysis_export
		self.result_export = self.result_fifo.analysis_export

	def check_phase(self):
		while self.result_fifo.can_get():
			_, actual = self.result_fifo.try_get()
			got_cmd, cmd = self.cmd_fifo.try_get()
			assert got_cmd
			expected = predict(cmd)
			assert expected == actual, f"cmd={cmd} expected={expected} actual={actual}"
```

Code walkthrough:

`CmdMonitor` and `ResultMonitor` are passive observers. They create analysis ports in `build_phase` and continuously publish observed values in `run_phase`. They do not drive DUT behavior.

`AluScoreboard` builds two analysis FIFOs, one for commands and one for results. This pattern handles producer-consumer rate differences while preserving ordering assumptions needed for comparison.

In `check_phase`, the scoreboard drains result data, fetches the corresponding command, computes the predicted value, and asserts on mismatch. This is the central UVM checking pattern: expected-versus-actual at a dedicated checker boundary.

Example env wiring:

```python
def connect_phase(self):
	self.cmd_mon.ap.connect(self.scoreboard.cmd_export)
	self.result_mon.ap.connect(self.scoreboard.result_export)
```

Code walkthrough:

This wiring defines the analysis topology. Command monitor output goes to the command input of the scoreboard, and result monitor output goes to the result input.

Placing these connects in `connect_phase` ensures all components exist before wiring occurs, which avoids intermittent startup failures and aligns with UVM phase discipline.

## Step 1: add monitor

Create monitor with `uvm_analysis_port` and publish observed tuples.

Checkpoint: monitor emits expected number of observations.

## Step 2: add scoreboard

Use analysis FIFO(s) or analysis exports to consume monitor output and compare expected versus actual.

Checkpoint: pass logs for matching transactions.

## Step 3: wire env connections

Connect monitor analysis port to scoreboard export/analysis path in `connect_phase`.

Checkpoint: no connection mismatch error.

## Step 4: force one mismatch

Inject one incorrect expected result to validate scoreboard fail reporting.

Checkpoint: clear mismatch log with operation context.

## What you learned

- Monitor as passive observer
- Analysis broadcast patterns
- Deterministic scoreboard comparison loop

Module mapping:

- TLM interfaces: `pyuvm._s12_uvm_tlm_interfaces`
- Components and scoreboards: `pyuvm._s13_predefined_component_classes`
