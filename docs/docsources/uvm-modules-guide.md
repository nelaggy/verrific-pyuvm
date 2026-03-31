# UVM Modules in pyuvm

Audience: users who want to understand pyuvm by module family, not only by class name.

This page maps the major pyuvm implementation modules to UVM concepts and practical usage.

In many beginner guides, UVM is introduced as a list of classes. That works for first contact, but it quickly becomes limiting because it hides the system-level design of UVM. In real projects, you do not use one class at a time; you use coordinated subsystems: phasing, hierarchy, stimulus, communication, and checking.

pyuvm preserves that architectural model while adapting it to Python and cocotb. The result is easier to write and read than classic macro-heavy SV-UVM code, but the conceptual structure is still UVM. Understanding the structure by module family helps you scale from toy examples to maintainable verification environments.

## How to read module names

The pyuvm package uses section-based modules that align with IEEE 1800.2 areas:

- `_s05_*`: base classes
- `_s06_*`: reporting
- `_s08_*`: factory
- `_s09_*`: phasing
- `_s10_*`: synchronization/callbacks
- `_s12_*`: TLM
- `_s13_*`: predefined components and hierarchy
- `_s14_15_*`: sequences and sequencers
- `_reg/*`: register abstraction layer

## Base classes: object identity and common behavior

Primary module:

- `pyuvm._s05_base_classes`

Key classes:

- `uvm_object`
- `uvm_transaction`
- `uvm_field_op`

Why it matters:

- Almost all user-defined verification objects derive from this foundation.
- Naming, identity, and base behavior consistency start here.

The base classes are where UVM's object model begins. `uvm_object` gives you common naming and object identity behavior, while `uvm_transaction` establishes the idea that verification data should be represented as objects rather than loose dictionaries or ad hoc tuples. This is a core UVM design choice because transactions can be compared, logged, copied, randomized, and passed through infrastructure in a consistent way.

When teams skip this layer and pass raw structures around, environments become brittle. Scoreboards, monitors, and sequence libraries all start re-implementing compatibility logic. By committing to `uvm_object`-derived entities early, you build a stable contract that allows other UVM subsystems to function correctly.

In practical terms, this module is where beginners should establish naming conventions and transaction field conventions. Even if the first bench is small, this discipline prevents painful rewrites when the bench grows.

## Reporting: structured runtime observability

Primary module:

- `pyuvm._s06_reporting_classes`

Key class:

- `uvm_report_object`

Why it matters:

- pyuvm uses Python logging semantics through UVM-oriented objects.
- Every major component should produce actionable logs at the right level.

Reporting is not just about printing messages. In UVM, reporting is how you turn long async simulation behavior into diagnosable evidence. pyuvm integrates with Python logging, which means you get familiar logging controls while still using UVM-style component context.

Good reporting design separates flow logs from correctness logs. Flow logs show where the test is in the scenario lifecycle, while correctness logs explain mismatches with enough metadata to reproduce failures. Teams that invest in this separation reduce debug time dramatically.

This module also supports scalable regression operation: log levels can be tuned for smoke, nightly, or debug runs without rewriting test logic. That is a major operational benefit in large verification projects.

## Factory: runtime substitution and reuse scaling

Primary module:

- `pyuvm._s08_factory_classes`

Key class:

- `uvm_factory`

Why it matters:

- Enables high reuse: swap sequence, driver, or monitor variants without rewriting env topology.

Factory usage is a defining UVM capability: it allows you to keep environment structure stable while swapping behavior at runtime. This is how mature testbenches support many scenarios without cloning whole environments.

The key design principle is that tests own variation policy. Components should be reusable and mostly variation-agnostic, while tests apply overrides and configuration to produce scenario variants. This keeps responsibilities clean and avoids hardcoding test intent into reusable blocks.

Common failures in factory usage are almost always about ordering and paths: overrides applied too late, or instance paths that do not match actual hierarchy names. Treat override setup as part of explicit test setup, and log active overrides during bring-up.

## Phasing: lifecycle orchestration

Primary module:

- `pyuvm._s09_phasing`

Key classes:

- `uvm_build_phase`
- `uvm_connect_phase`
- `uvm_run_phase`
- `uvm_check_phase`
- `uvm_report_phase`

Why it matters:

- Prevents race-prone ad hoc initialization and execution.
- Gives deterministic framework points for structure, wiring, runtime, and closure.

Phasing is UVM's solution to a universal problem: when many components run concurrently, implicit ordering assumptions become bugs. The phase model creates deterministic hand-off points so component creation, connection, stimulus execution, and final checking do not race each other.

In pyuvm, this model maps naturally to Python methods and async coroutines. Build and connect phases define structure and wiring, while `run_phase` handles timed behavior. This separation is crucial: if users mix timed and structural logic carelessly, they get intermittent failures that are hard to reproduce.

Objections are part of phase control, not an optional add-on. They define test liveness. A high-quality bench has clear objection ownership and clear drop guarantees, including failure and exception paths.

## Synchronization and callbacks

Primary module:

- `pyuvm._s10_synchronization_classes`

Key classes/functions:

- `uvm_callback`
- `uvm_callbacks`
- `uvm_do_callbacks`

Why it matters:

- Supports extension hooks without deep inheritance chains.

Callbacks provide controlled extension points in reusable components. Instead of subclassing one component for every small behavior change, you can expose callback hooks and register policy-specific behavior per test or environment.

This matters for team-scale reuse. Different products, protocol options, or debug needs can share one component implementation while customizing only the extension points. The alternative, subclass explosion, quickly becomes hard to maintain.

Synchronization concerns still apply: callback side effects should be constrained and well documented. If callbacks mutate shared state unpredictably, they become another source of nondeterministic bugs.

## TLM: communication contracts between components

Primary module:

- `pyuvm._s12_uvm_tlm_interfaces`

Key classes:

- `uvm_analysis_port`
- `uvm_tlm_fifo`
- blocking/non-blocking put/get/peek ports and exports

Why it matters:

- Separates producers and consumers cleanly.
- Makes monitor-to-scoreboard and sequencer-to-driver paths explicit.

TLM is one of the most important UVM ideas. It decouples components through interface contracts rather than direct references. A producer should not need to know the internals of its consumers, and consumers should not need to control producer timing.

In pyuvm, TLM ports, exports, and FIFOs make that contract explicit. Analysis ports are especially important because they support passive observation fanout: one monitor can feed scoreboard, coverage, and debug subscribers simultaneously.

Most TLM integration issues are contract mismatches: wrong interface type, wrong connection phase, or blocking assumptions that do not hold. Treat TLM connections as first-class design artifacts, not incidental plumbing.

## Components and hierarchy

Primary modules:

- `pyuvm._s13_predefined_component_classes`
- `pyuvm._s13_uvm_component`

Key classes:

- `uvm_component`
- `uvm_test`, `uvm_env`, `uvm_agent`, `uvm_driver`, `uvm_monitor`, `uvm_scoreboard`
- `ConfigDB`
- `uvm_root`

Why it matters:

- Defines architecture, ownership boundaries, and discoverable hierarchy paths.

Component hierarchy is where UVM becomes a system architecture instead of a script. `uvm_test` owns scenario intent, `uvm_env` owns composition, agents own protocol behavior, and scoreboards own correctness decisions. Keeping these boundaries clear is the strongest predictor of long-term maintainability.

Hierarchy also drives discoverability and configuration. Paths are not just names: they are used for ConfigDB targeting, instance overrides, and debug context. Consistent hierarchy naming pays off every day in bring-up and regression triage.

Teams new to UVM often over-centralize logic in the test class. Resist that pattern. Tests should orchestrate and configure; reusable behavior belongs in components and sequences.

## Sequences and sequencers

Primary module:

- `pyuvm._s14_15_python_sequences`

Key classes:

- `uvm_sequence_item`
- `uvm_sequence`
- `uvm_sequencer`
- `ResponseQueue`

Why it matters:

- Encodes stimulus intent in reusable transactions and scenarios.
- Separates scenario generation from protocol driving.

Sequences are UVM's stimulus language. They describe what should happen as transaction intent, while drivers describe how that intent is translated into protocol signaling. This split is critical for reuse: a scenario can outlive a specific driver implementation.

Sequencers provide arbitration and flow control between multiple sequences. In simple benches this may feel unnecessary, but in realistic verification it prevents ad hoc contention logic and supports layered stimulus generation.

A strong sequence library usually includes directed smoke flows, constrained-random flows, and composed scenario flows. Keeping these in sequence space, not in test classes, keeps regressions scalable.

## Register abstraction layer (RAL)

Primary modules:

- `pyuvm._reg.uvm_reg`
- `pyuvm._reg.uvm_reg_field`
- `pyuvm._reg.uvm_reg_block`
- `pyuvm._reg.uvm_reg_map`
- `pyuvm._reg.uvm_reg_adapter`
- `pyuvm._reg.uvm_reg_predictor`

Why it matters:

- Enables register-centric verification with frontdoor/backdoor abstractions.
- Aligns software-visible behavior checks with bus-level interactions.

RAL provides a software-like abstraction for register verification while preserving hardware transport realism. Users can reason about register intent (read/write/predict) without hardcoding every bus transaction sequence in every test.

Adapters bridge abstract register operations to concrete bus operations. Predictors and callbacks keep model state aligned with observed behavior. This layered model is especially valuable when the same register map is accessed through different frontdoors or mixed with backdoor checks.

For beginners, the practical entry point is command/status/result loops with explicit timeouts and robust mismatch logs. Full RAL depth can come later, but even simple adoption improves clarity and reuse.

## Practical order for module learning

1. `_s13` components and hierarchy
2. `_s09` phasing
3. `_s14_15` sequences
4. `_s12` TLM
5. `_s08` factory
6. `_s10` callbacks
7. `_reg` modules when register verification is needed

This order is deliberate: it follows the lifecycle of most verification projects. You first need architecture and execution control, then stimulus and communication, then variation mechanisms, and finally specialized subsystems like callbacks and RAL.

If you are migrating from SV-UVM, the same order still works, but pay extra attention to async semantics in run paths and explicit `await` usage in sequence and monitor flows.

## Related pages

- [Components Guide](components-guide.md)
- [Phasing Guide](phasing-guide.md)
- [Sequences Guide](sequences-guide.md)
- [TLM Guide](tlm-guide.md)
- [Advanced API Reference](reference-advanced.md)
