# FAQ

## Is pyuvm only for users with SystemVerilog UVM background?

No. Python developers can use pyuvm directly. Knowing verification concepts helps, but the guides in this documentation are written for Python-first onboarding.

## Do I need macros like in SV UVM?

No. pyuvm uses Python class behavior and automatic registration patterns; macro-heavy setup is not required.

## Why does my test hang even when code looks correct?

Most hangs come from objection mismatches or incomplete sequence-driver handshake (`get_next_item`/`item_done`). See [Troubleshooting](troubleshooting.md).

## Where should I start: examples or reference docs?

Start with [Quickstart](quickstart.md), then [Core Concepts](concepts-index.md), then [Tutorial Track](tutorials-index.md). Use reference docs as lookup material during implementation.

## Does pyuvm include full register model support?

pyuvm includes broad RAL support, but not every edge feature is complete. Use [Tutorial 4](tutorial-4-register-model-basics.md) and [RAL Read/Write recipe](recipes-ral-read-write.md) for practical usage first.
