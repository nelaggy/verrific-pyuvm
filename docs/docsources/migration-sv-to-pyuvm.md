# Migration: SystemVerilog UVM to pyuvm

Audience: verification engineers experienced with SV UVM who are moving to Python.

## Concept mapping

| SV UVM idea | pyuvm equivalent |
|---|---|
| `uvm_component_utils` macros | automatic registration for classes derived from `uvm_void` |
| `uvm_config_db` | `ConfigDB()` singleton |
| task-based run phase | async `run_phase` coroutine |
| sequence/sequencer handshake | `start_item`/`finish_item` and `get_next_item`/`item_done` |
| UVM reporting macros | Python logging through `self.logger` |

## What changes the most

1. Concurrency model

- In pyuvm, blocking operations are explicit with `await`.
- If you forget `await`, behavior fails silently or deadlocks later.

2. Type system

- Python is dynamic; many typing errors are runtime errors.
- You gain flexibility but must rely more on tests and assertions.

3. Error handling

- pyuvm uses Python exceptions (`UVM*Error` classes).
- Prefer failing early with clear assertion/error messages.

## Migration checklist

- Replace macro registration assumptions with class inheritance checks.
- Audit all timed paths for async correctness.
- Confirm objection handling in every test entry path.
- Validate ConfigDB scope patterns (`*` path usage).
- Add sequence-driver handshake assertions while migrating.

## Recommended migration order

1. Port one minimal directed test.
2. Port one constrained/random sequence flow.
3. Port monitor + scoreboard data path.
4. Port factory override variants.
5. Port register model usage if needed.

## Common migration mistakes

- Treating `run_phase` as synchronous code.
- Assuming compile-time type catches for TLM mismatch.
- Applying overrides with incorrect instance path patterns.
