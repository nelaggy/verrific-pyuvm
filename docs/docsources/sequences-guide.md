# Sequences Guide

Audience: users authoring transaction stimulus and sequence composition.

UVM idea introduced: transaction intent separated from signal driving.

In UVM architecture, sequences describe what should happen, while drivers implement how protocol signaling happens. This separation is key for reuse across tests.

## Sequence flow

1. Create item (`uvm_sequence_item`).
2. `await start_item(item)`.
3. Populate/adjust item fields.
4. `await finish_item(item)`.
5. Driver receives via `get_next_item()` and completes with `item_done()`.

## Minimal sequence

```python
class AddSeq(uvm_sequence):
    async def body(self):
        item = AluItem("add")
        item.a = 3
        item.b = 5
        item.op = "ADD"
        await self.start_item(item)
        await self.finish_item(item)
```

## Driver-side handshake

```python
item = await self.seq_item_port.get_next_item()
# drive DUT
self.seq_item_port.item_done()
```

## Composition patterns

- Directed sequence: deterministic values.
- Random sequence: value randomization each iteration.
- Scenario sequence: compose helper operations into algorithm flows.

## Pitfalls

- Calling `finish_item` without a corresponding driver handshake.
- Missing `await` on `start_item` or `finish_item`.
- Assuming FIFO response order when sequences run concurrently.

Module mapping:

- Sequence and sequencer implementation: `pyuvm._s14_15_python_sequences`
- Sequence-related errors: `pyuvm._error_classes`

## Related pages

- [Recipe: Sequence Patterns](recipes-sequence-patterns.md)
- [Tutorial 3](tutorial-3-sequence-composition.md)
