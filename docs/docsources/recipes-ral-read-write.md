# Recipe: RAL Read/Write Loop

Task: perform command-style register programming with done polling.

## Pattern

1. Write source/config register.
2. Write command/start register.
3. Poll command/status register until done bit set.
4. Read result register and compare expected value.

## Pseudocode

```python
await reg_write(SRC_ADDR, src)
await reg_write(CMD_ADDR, start_cmd)
while True:
    status = await reg_read(CMD_ADDR)
    if done(status):
        break
result = await reg_read(RESULT_ADDR)
assert result == expected
```

## Checklist

- Add timeout to poll loop.
- Report status and command on timeout.
- Keep adapter translation logic isolated and testable.
