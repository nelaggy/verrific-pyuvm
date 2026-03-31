# Core API Reference

This page groups the most-used pyuvm symbols by workflow.

## Build testbench structure

- `uvm_test`
- `uvm_env`
- `uvm_agent`
- `uvm_component`

## Drive stimulus

- `uvm_sequence_item`
- `uvm_sequence`
- `uvm_sequencer`
- `uvm_driver`
- `uvm_seq_item_port`
- `uvm_seq_item_export`

## Observe and check

- `uvm_monitor`
- `uvm_scoreboard`
- `uvm_subscriber`
- `uvm_analysis_port`
- `uvm_tlm_analysis_fifo`

## Configure

- `ConfigDB`
- `uvm_config_db`

## Lifecycle control

- `uvm_build_phase`
- `uvm_connect_phase`
- `uvm_run_phase`
- `raise_objection` and `drop_objection` methods on components

## Key exceptions

- `UVMError`
- `UVMConfigError`
- `UVMConfigItemNotFound`
- `UVMSequenceError`

For full signatures and inherited members, use generated API docs in `apidocs/index`.
