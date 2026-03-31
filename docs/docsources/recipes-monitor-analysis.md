# Recipe: Monitor to Analysis Wiring

Task: publish observed DUT transactions to downstream checkers.

## Template

```python
class CmdMonitor(uvm_component):
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)

    async def run_phase(self):
        while True:
            cmd = await self.bfm.get_cmd()
            self.ap.write(cmd)
```

In env `connect_phase`:

```python
self.cmd_mon.ap.connect(self.scoreboard.cmd_export)
```

## Checklist

- Monitor is passive (no DUT driving).
- Analysis port created in `build_phase`.
- Connect performed in `connect_phase`.
