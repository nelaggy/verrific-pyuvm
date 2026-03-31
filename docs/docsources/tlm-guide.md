# TLM Guide

Audience: users wiring communication between pyuvm components.

UVM idea introduced: interface-based communication decoupling.

TLM is central to UVM scalability: components communicate through abstract interfaces instead of direct coupling. This enables substitution, monitoring, and reuse with minimal rewiring.

## Core TLM concepts

- Port: initiates communication.
- Export/imp: receives communication.
- Analysis port: broadcast channel for non-blocking observation flows.

## Commonly used interfaces

- `uvm_blocking_put_port` / `uvm_blocking_put_export`
- `uvm_blocking_get_port` / `uvm_blocking_get_export`
- `uvm_analysis_port`, `uvm_analysis_export`, `uvm_analysis_imp`
- `uvm_tlm_fifo`, `uvm_tlm_analysis_fifo`

## Typical analysis pattern

```python
class MyMonitor(uvm_component):
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)

# In env connect_phase:
self.monitor.ap.connect(self.scoreboard.analysis_export)
```

## FIFO pattern

Use `uvm_tlm_analysis_fifo` when producer and consumer run at different rates and ordering matters.

## Pitfalls

- Connecting incompatible interface types.
- Doing connect calls outside `connect_phase`.
- Blocking forever due to missing producer writes.

Module mapping:

- TLM interfaces and channels: `pyuvm._s12_uvm_tlm_interfaces`
- Connection error types: `UVMTLMConnectionError` in `pyuvm._error_classes`

## Related pages

- [Recipe: Monitor to Analysis Wiring](recipes-monitor-analysis.md)
- [Recipe: Scoreboard Patterns](recipes-scoreboard-patterns.md)
