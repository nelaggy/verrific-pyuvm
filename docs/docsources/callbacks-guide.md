# Callbacks Guide

Audience: users adding extension points to reusable verification components.

## Callback model

- Define callback class derived from `uvm_callback`.
- Register callback implementations with `uvm_callbacks`.
- Invoke hooks from the host component via callback utilities.

## When to use callbacks

- Optional behavior injection without subclass explosion.
- Fine-grained event hooks for checking, logging, or metrics.

## Safety guidelines

- Keep callback side effects small and explicit.
- Avoid mutating callback registration while iterating callbacks.
- Document callback ordering assumptions.

## Minimal flow

1. Define callback interface methods.
2. Register callback instances in setup.
3. Invoke callbacks at stable points in component logic.

## Related pages

- [Advanced API Reference](reference-advanced.md)
