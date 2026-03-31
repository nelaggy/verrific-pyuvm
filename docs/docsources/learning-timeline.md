# Learning Timeline

Audience: Python users who want a structured path into UVM and pyuvm.

Outcome: move from first test bring-up to advanced reusable verification patterns.

## Week 1: UVM fundamentals in Python

Goals:

- Understand what UVM solves: reuse, layering, scalability.
- Learn pyuvm component graph and phase flow.
- Run your first passing test.

Read and do:

1. [Quickstart](quickstart.md)
2. [Getting Started](getting-started.md)
3. [Components Guide](components-guide.md)
4. [Phasing Guide](phasing-guide.md)
5. [Tutorial 1: Minimal Environment](tutorial-1-minimal-env.md)

Deliverable:

- A minimal testbench that sends at least one transaction and exits cleanly.

## Week 2: Dataflow and checking

Goals:

- Understand sequence-driver handshake.
- Build monitor and scoreboard dataflow.
- Diagnose mismatch failures quickly.

Read and do:

1. [Sequences Guide](sequences-guide.md)
2. [TLM Guide](tlm-guide.md)
3. [ConfigDB Guide](configdb-guide.md)
4. [Tutorial 2: Scoreboard and Analysis](tutorial-2-scoreboard-and-analysis.md)
5. [Tutorial 3: Sequence Composition](tutorial-3-sequence-composition.md)

Deliverable:

- A testbench with passive monitor checks and at least one composed scenario sequence.

## Week 3: Reuse and variants

Goals:

- Use factory overrides for test variants.
- Introduce negative tests safely.
- Build regression-friendly structure.

Read and do:

1. [Factory Guide](factory-guide.md)
2. [Callbacks Guide](callbacks-guide.md)
3. [Tutorial 5: Advanced Test Variants](tutorial-5-advanced-test-variants.md)
4. [Recipes](recipes-index.md)

Deliverable:

- A baseline test plus at least one stress variant and one expected-failure variant.

## Week 4: Register-layer workflows

Goals:

- Understand practical RAL usage patterns.
- Build frontdoor write/poll/read loops.
- Integrate register checks into scoreboard/reporting.

Read and do:

1. [Advanced API Reference](reference-advanced.md)
2. [Tutorial 4: Register Model Basics](tutorial-4-register-model-basics.md)
3. [Recipe: RAL Read/Write Loop](recipes-ral-read-write.md)

Deliverable:

- A register-driven scenario with deterministic completion and clear timeout handling.

## Optional parallel track: migration from SV UVM

Read:

1. [Migration: SystemVerilog UVM to pyuvm](migration-sv-to-pyuvm.md)
2. [UVM and Python](UVM_and_Python.rst)

Use this track to translate existing SV-UVM habits into Python async patterns.
