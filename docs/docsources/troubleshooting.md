# Troubleshooting

This page collects common pyuvm runtime failures and practical fixes.

## Symptom: test never ends

Likely causes:

- Missing `drop_objection()`.
- Driver not calling `item_done()`.
- Sequence waiting on a handshake that never occurs.

Checks:

1. Verify every `raise_objection()` has a matching drop path.
2. Verify driver loop always reaches `item_done()`.
3. Add temporary logs around sequence/driver handshake points.

## Symptom: test ends immediately

Likely causes:

- No objection raised in run path.
- Sequence failed before workload started.

Checks:

1. Raise objection before first awaited sequence action.
2. Wrap test body with clear fail-fast assertions.

## Symptom: ConfigDB lookup fails

Likely causes:

- Incorrect instance path or wildcard.
- Key mismatch by name.

Checks:

1. Confirm exact key string parity between `set` and `get`.
2. Start with explicit instance path, then widen with wildcard.
3. Log component full name during lookup.

## Symptom: connection/type errors

Likely causes:

- Incompatible port/export wiring.
- Wrong connect phase order.

Checks:

1. Perform all TLM connects in `connect_phase`.
2. Check that each producer/consumer pair uses matching interface type.

## Symptom: out-of-order response confusion

Likely causes:

- Multiple concurrent sequences with FIFO-only response handling.

Checks:

1. Use transaction identifiers for response matching.
2. Keep deterministic sequencing during initial bring-up.
