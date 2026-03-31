# API Reference: Core

Auto-generated API reference for core user-facing pyuvm classes and functions (components, phasing, sequences, factory, configuration, reporting).

Type legend:

- `object`: no explicit annotation was available; type inferred from docs/defaults/name where possible.
- `required` default: argument has no default and must be supplied by caller.

## Coverage

- Symbols in this page: `45`
- Classes: `44`
- Functions/callables: `0`
- Constants/other values: `1`

## Index

### Classes

- `ConfigDB`
- `ResponseQueue`
- `UVMBadPhase`
- `UVMConfigItemNotFound`
- `UsePythonMethod`
- `uvm_active_passive_enum`
- `uvm_agent`
- `uvm_bottomup_phase`
- `uvm_build_phase`
- `uvm_callback`
- `uvm_callback_iter`
- `uvm_callbacks`
- `uvm_check_phase`
- `uvm_component`
- `uvm_connect_phase`
- `uvm_driver`
- `uvm_end_of_elaboration_phase`
- `uvm_env`
- `uvm_extract_phase`
- `uvm_factory`
- `uvm_field_op`
- `uvm_final_phase`
- `uvm_monitor`
- `uvm_object`
- `uvm_phase`
- `uvm_policy`
- `uvm_report_object`
- `uvm_report_phase`
- `uvm_root`
- `uvm_run_phase`
- `uvm_scoreboard`
- `uvm_seq_item_export`
- `uvm_seq_item_port`
- `uvm_sequence`
- `uvm_sequence_base`
- `uvm_sequence_item`
- `uvm_sequencer`
- `uvm_sequencer_base`
- `uvm_start_of_simulation_phase`
- `uvm_subscriber`
- `uvm_test`
- `uvm_threaded_execute_phase`
- `uvm_topdown_phase`
- `uvm_transaction`

### Functions


### Constants

- `uvm_common_phases`

## Class `ConfigDB`

Module: `pyuvm`

No description available.

### Constructor

Signature: `ConfigDB(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `ConfigDB` instance

### Methods

#### `ConfigDB.clear`

Reset the ConfigDB. Used for testing.

Signature: `clear(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `ConfigDB.exists`

Returns true if there is data in the database at this location

Signature: `exists(self, context, inst_name, field_name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `context` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | None or uvm_component |
| `inst_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | instance name string in context |
| `field_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | key name for location |

Output: `object`

#### `ConfigDB.get`

The component path matches against the paths in the ConfigDB. The path

Signature: `get(self, context, inst_name, field_name, default=<object object at 0x1040f4cb0>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `context` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component making the call |
| `inst_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | component full path with no wildcards |
| `field_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | the field_name being retrieved |
| `default` | `POSITIONAL_OR_KEYWORD` | `object` | `<object object at 0x1040f4cb0>` | the value to return if there is no key, defaults to |

Output: `object`

#### `ConfigDB.set`

Stores an object in the db using the context and

Signature: `set(self, context, inst_name, field_name, value)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `context` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | A handle to a component |
| `inst_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The instance name within the component |
| `field_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The key we're setting |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to be stored |

Output: `object`

#### `ConfigDB.trace`

Output the ConfigDB activity if tracing is on.

Signature: `trace(self, method, context, inst_name, field_name, value)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `method` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `context` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |
| `inst_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `field_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `ConfigDB.wait_modified`

No description available.

Signature: `wait_modified(self, context, inst_name, field_name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `context` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |
| `inst_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `field_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

## Class `ResponseQueue`

Module: `pyuvm`

The ``ResponseQueue`` is a queue that can cherry-pick an item

### Constructor

Signature: `ResponseQueue(self, maxsize: int = 0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maxsize` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `ResponseQueue` instance

### Methods

#### `ResponseQueue.empty`

Return ``True`` if the queue is empty, ``False`` otherwise.

Signature: `empty(self) -> bool`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `ResponseQueue.full`

Return ``True`` if there are :meth:`maxsize` items in the queue.

Signature: `full(self) -> bool`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `ResponseQueue.get`

Remove and return an item from the queue.

Signature: `get(self) -> ~T`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `~T`

#### `ResponseQueue.get_nowait`

Remove and return an item from the queue.

Signature: `get_nowait(self) -> ~T`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `~T`

#### `ResponseQueue.get_response`

A coroutine that will either get a response item with

Signature: `get_response(self, txn_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | (Optional) The transaction ID of the response you want |

Output: `object`

#### `ResponseQueue.peek`

Remove and return an item from the queue.

Signature: `peek(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `ResponseQueue.peek_nowait`

Remove and return an item from the queue.

Signature: `peek_nowait(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `ResponseQueue.put`

Put an *item* into the queue.

Signature: `put(self, item: ~T) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `~T` | `required` | Parameter. |

Output: `None`

#### `ResponseQueue.put_nowait`

Extend the ``cocotb.queue.Queue.put_nowait`` method to set the

Signature: `put_nowait(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The item to put in the queue |

Output: `None`

#### `ResponseQueue.qsize`

Number of items in the queue.

Signature: `qsize(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

## Class `UVMBadPhase`

Module: `pyuvm`

Errors in phasing

### Constructor

Signature: `UVMBadPhase(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMBadPhase` instance

### Methods

#### `UVMBadPhase.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMBadPhase.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMConfigItemNotFound`

Module: `pyuvm`

Couldn't find something in config_db

### Constructor

Signature: `UVMConfigItemNotFound(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMConfigItemNotFound` instance

### Methods

#### `UVMConfigItemNotFound.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMConfigItemNotFound.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UsePythonMethod`

Module: `pyuvm`

For cases where the user should use a Python

### Constructor

Signature: `UsePythonMethod(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UsePythonMethod` instance

### Methods

#### `UsePythonMethod.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UsePythonMethod.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `uvm_active_passive_enum`

Module: `pyuvm`

Enum where members are also (and must be) ints

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_PASSIVE` | `0` | Enum member. |
| `UVM_ACTIVE` | `1` | Enum member. |

## Class `uvm_agent`

Module: `pyuvm`

The :class:`!uvm_agent` virtual class should be used as the base class for

### Constructor

Signature: `uvm_agent(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_agent` instance

### Methods

#### `uvm_agent.active`

No description available.

Signature: `active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_agent.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_agent.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_agent.build_phase`

This ``build_phase()`` implements agent-specific behavior.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_agent.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_agent.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_agent.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_agent.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_agent.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_agent.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_agent.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_agent.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_agent.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_agent.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_is_active`

Returns :data:`~uvm_active_passive_enum.UVM_ACTIVE` if the agent is

Signature: `get_is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_agent.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_agent.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_agent.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_agent.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_agent.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_agent.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_agent.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_agent.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_agent.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_agent.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_agent.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_agent.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_bottomup_phase`

Module: `pyuvm`

Runs the phases from bottom up.

### Constructor

Signature: `uvm_bottomup_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_bottomup_phase` instance

### Methods

#### `uvm_bottomup_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_bottomup_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_bottomup_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_bottomup_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_bottomup_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_bottomup_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_bottomup_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_bottomup_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_bottomup_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_bottomup_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_bottomup_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_bottomup_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_bottomup_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_build_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_build_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_build_phase` instance

### Methods

#### `uvm_build_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_build_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_build_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_build_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_build_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_build_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_build_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_build_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_build_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_build_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_build_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_build_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_build_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_callback`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_callback(self, name: 'str' = 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callback'` | Name of the object. Default is empty string. |

Output: `uvm_callback` instance

### Methods

#### `uvm_callback.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_callback.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_callback.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_callback.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_callback.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_callback.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_callback.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_callback.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_callback.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_callback.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_callback.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_callback.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callback.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_callback_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_callback_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_callback_iter` instance

### Methods

#### `uvm_callback_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_callback_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_callback_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_callback_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_callback_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_callbacks`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_callbacks(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_callbacks` instance

### Methods

#### `uvm_callbacks.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_callbacks.add_by_name`

No description available.

Signature: `add_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component', ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `None`

#### `uvm_callbacks.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_callbacks.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_callbacks.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_callbacks.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_callbacks.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_callbacks.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_callbacks.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_callbacks.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_callbacks.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_callbacks.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_callbacks.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_callbacks.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_callbacks.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_callbacks.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_callbacks.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_callbacks.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_callbacks.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_callbacks.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_check_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_check_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_check_phase` instance

### Methods

#### `uvm_check_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_check_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_check_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_check_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_check_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_check_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_check_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_check_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_check_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_check_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_check_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_check_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_check_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_component`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_component(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_component` instance

### Methods

#### `uvm_component.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_component.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_component.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_component.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_component.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_component.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_component.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_component.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_component.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_component.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_component.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_component.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_component.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_component.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_component.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_component.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_component.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_component.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_component.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_component.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_component.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_component.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_component.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_component.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_component.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_component.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_connect_phase`

Module: `pyuvm`

Runs the phases from bottom up.

### Constructor

Signature: `uvm_connect_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_connect_phase` instance

### Methods

#### `uvm_connect_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_connect_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_connect_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_connect_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_connect_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_connect_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_connect_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_connect_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_connect_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_connect_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_connect_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_connect_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_connect_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_driver`

Module: `pyuvm`

The base class for drivers that initiate requests for new transactions via

### Constructor

Signature: `uvm_driver(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `uvm_driver` instance

### Methods

#### `uvm_driver.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_driver.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_driver.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_driver.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_driver.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_driver.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_driver.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_driver.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_driver.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_driver.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_driver.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_driver.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_driver.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_driver.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_driver.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_driver.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_driver.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_driver.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_driver.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_driver.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_driver.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_driver.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_driver.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_driver.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_driver.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_driver.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_end_of_elaboration_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_end_of_elaboration_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_end_of_elaboration_phase` instance

### Methods

#### `uvm_end_of_elaboration_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_end_of_elaboration_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_end_of_elaboration_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_end_of_elaboration_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_end_of_elaboration_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_end_of_elaboration_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_end_of_elaboration_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_end_of_elaboration_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_env`

Module: `pyuvm`

The base class for hierarchical containers of other components that

### Constructor

Signature: `uvm_env(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_env` instance

### Methods

#### `uvm_env.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_env.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_env.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_env.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_env.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_env.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_env.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_env.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_env.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_env.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_env.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_env.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_env.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_env.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_env.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_env.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_env.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_env.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_env.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_env.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_env.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_env.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_env.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_env.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_env.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_env.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_extract_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_extract_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_extract_phase` instance

### Methods

#### `uvm_extract_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_extract_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_extract_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_extract_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_extract_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_extract_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_extract_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_extract_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_extract_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_extract_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_extract_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_extract_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_extract_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_factory`

Module: `pyuvm`

The uvm_factory is a singleton that delivers all UVM factory functions.

### Constructor

Signature: `uvm_factory(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_factory` instance

### Methods

#### `uvm_factory.clear_all`

Clear all the classes and overrides from the factory

Signature: `clear_all(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_factory.clear_overrides`

Clear all the overrides from the factory

Signature: `clear_overrides(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_factory.create_component_by_name`

Create a components using the name of the requested uvm_component type

Signature: `create_component_by_name(self, requested_type_name, parent_inst_path='', name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | the type that could be overridden |
| `parent_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A path if we are checking for inst overrides |
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The name of the new object. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | The component's parent component |

Output: `object`

#### `uvm_factory.create_component_by_type`

:param requested_type: Type type to be overridden

Signature: `create_component_by_type(self, requested_type, parent_inst_path='', name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Type type to be overridden |
| `parent_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The inst path if we are looking |
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Concatenated with parent_inst_path if it |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | The parent component |

Output: `object`

#### `uvm_factory.create_object_by_name`

:param requested_type_name: the type that could be overridden

Signature: `create_object_by_name(self, requested_type_name, parent_inst_path='', name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | the type that could be overridden |
| `parent_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A path if we are checking for inst overrides |
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The name of the new object. |

Output: `object`

#### `uvm_factory.create_object_by_type`

:param requested_type: The type that we request but that can be

Signature: `create_object_by_type(self, requested_type, parent_inst_path='', name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The type that we request but that can be |
| `parent_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The get_full_name path of the parent |
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The name of the instance requested_type("name") |

Output: `object`

#### `uvm_factory.find_override_by_name`

:param requested_type_name:

Signature: `find_override_by_name(self, requested_type_name, full_inst_path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `full_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_factory.find_override_by_type`

:param requested_type: The type whose override you want

Signature: `find_override_by_type(self, requested_type, full_inst_path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The type whose override you want |
| `full_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The inst path where one looks |

Output: `object`

#### `uvm_factory.find_wrapper_by_name`

:raises: UVMNotImplemented There are no wrappers in

Signature: `find_wrapper_by_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_factory.is_type_name_registered`

:param type_name: string that is name of a type

Signature: `is_type_name_registered(self, type_name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | string that is name of a type |

Output: `bool`

#### `uvm_factory.is_type_registered`

:param uvm_type: The type to be checked

Signature: `is_type_registered(self, uvm_type)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `uvm_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The type to be checked |

Output: `bool`

#### `uvm_factory.print`

:param debug_level:

Signature: `print(self, debug_level=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `debug_level` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |

Output: `object`

#### `uvm_factory.set_inst_alias`

:param alias_type_name:A string that will reference the original type

Signature: `set_inst_alias(self, alias_type_name, original_type, full_inst_path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `alias_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | A string that will reference the original type |
| `original_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The original type toe be referenced |
| `full_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The instance path where this alias is active |

Output: `None`

#### `uvm_factory.set_inst_override_by_name`

:param original_type_name: the name of type being replaced

Signature: `set_inst_override_by_name(self, original_type_name, override_type_name, full_inst_path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `original_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | the name of type being replaced |
| `override_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | the name of the substitute type |
| `full_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The path to the instance |

Output: `None`

#### `uvm_factory.set_inst_override_by_type`

:param original_type: The original type being overridden

Signature: `set_inst_override_by_type(self, original_type, override_type, full_inst_path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `original_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The original type being overridden |
| `override_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The overriding type |
| `full_inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The inst where this happens |

Output: `None`

#### `uvm_factory.set_type_alias`

:param alias_type_name:A string that will reference the original type

Signature: `set_type_alias(self, alias_type_name, original_type)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `alias_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | A string that will reference the original type |
| `original_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The original type toe be referenced |

Output: `None`

#### `uvm_factory.set_type_override_by_name`

:param original_type_name: The name of the type to be

Signature: `set_type_override_by_name(self, original_type_name, override_type_name, replace=True)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `original_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the type to be |
| `override_type_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the overriding type. |
| `replace` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | If the override already exists only replace |

Output: `None`

#### `uvm_factory.set_type_override_by_type`

:param original_type: The original type to be overridden

Signature: `set_type_override_by_type(self, original_type, override_type, replace=True)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `original_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The original type to be overridden |
| `override_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The new type that will override it |
| `replace` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | If the override exists, only replace it if this is True |

Output: `None`

## Class `uvm_field_op`

Module: `pyuvm`

We do not implement the UVM field op as this is a

### Constructor

Signature: `uvm_field_op(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_field_op` instance

## Class `uvm_final_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_final_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_final_phase` instance

### Methods

#### `uvm_final_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_final_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_final_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_final_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_final_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_final_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_final_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_final_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_final_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_final_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_final_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_final_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_final_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_monitor`

Module: `pyuvm`

This class should be used as the base class for user-defined monitors.

### Constructor

Signature: `uvm_monitor(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_monitor` instance

### Methods

#### `uvm_monitor.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_monitor.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_monitor.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_monitor.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_monitor.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_monitor.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_monitor.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_monitor.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_monitor.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_monitor.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_monitor.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_monitor.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_monitor.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_monitor.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_monitor.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_monitor.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_monitor.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_monitor.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_monitor.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_monitor.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_monitor.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_monitor.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_monitor.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_monitor.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_monitor.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_monitor.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_object`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_object(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_object` instance

### Methods

#### `uvm_object.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_object.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_object.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_object.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_object.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_object.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_object.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_object.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_object.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_object.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_phase`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_phase` instance

### Methods

#### `uvm_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_policy`

Module: `pyuvm`

The uvm_policy is used to add functionality to

### Constructor

Signature: `uvm_policy(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_policy` instance

## Class `uvm_report_object`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_report_object(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the object |

Output: `uvm_report_object` instance

### Methods

#### `uvm_report_object.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_report_object.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_report_object.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_report_object.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_report_object.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_report_object.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_report_object.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_report_object.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_report_object.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_report_object.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_report_object.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_report_object.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_report_object.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_report_object.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_object.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_report_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_report_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_report_phase` instance

### Methods

#### `uvm_report_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_report_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_report_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_report_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_report_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_report_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_report_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_report_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_report_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_report_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_report_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_report_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_report_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_root`

Module: `pyuvm`

F.7.  We do not use ``uvm_pkg`` to hold ``uvm_root``.  Instead it

### Constructor

Signature: `uvm_root(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_root` instance

### Methods

#### `uvm_root.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_root.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_root.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_root.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_root.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_root.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.clear_singletons`

Clear the singletons in the system.  This is used for testing

Signature: `clear_singletons(keep_set={})`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `keep_set` | `POSITIONAL_OR_KEYWORD` | `dict` | `{}` | Parameter. |

Output: `object`

#### `uvm_root.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_root.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_root.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_root.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_root.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_root.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_root.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_root.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.find`

find does a find_all with comp = None and returns the first element in

Signature: `find(self, comp_match: 'str') -> 'uvm_component | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp_match` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_component | None`

#### `uvm_root.find_all`

Returns a list of components matching a given comp_match string. Matches

Signature: `find_all(self, comp_match: 'str', comp: 'uvm_component | None' = None) -> 'list[uvm_component]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp_match` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component | None` | `None` | Parameter. |

Output: `list[uvm_component]`

#### `uvm_root.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_root.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_root.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_root.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_root.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_root.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_root.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.run_test`

:param test_name: The uvm test name or test class

Signature: `run_test(self, test_name, keep_singletons=False, keep_set=set())`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `test_name` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The uvm test name or test class |
| `keep_singletons` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | If True do not clear singletons (default False) |
| `keep_set` | `POSITIONAL_OR_KEYWORD` | `set` | `set()` | Set of singleton classes to keep |

Output: `object`

#### `uvm_root.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_root.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_root.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_root.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_root.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_root.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_root.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_root.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_run_phase`

Module: `pyuvm`

This phase launches the phase function in a thread and

### Constructor

Signature: `uvm_run_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_run_phase` instance

### Methods

#### `uvm_run_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_run_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_run_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_run_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_run_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_run_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_run_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_run_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_run_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_run_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_run_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_run_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_run_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_scoreboard`

Module: `pyuvm`

This class should be used as the base class for user-defined scoreboards.

### Constructor

Signature: `uvm_scoreboard(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_scoreboard` instance

### Methods

#### `uvm_scoreboard.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_scoreboard.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_scoreboard.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_scoreboard.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_scoreboard.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_scoreboard.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_scoreboard.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_scoreboard.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_scoreboard.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_scoreboard.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_scoreboard.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_scoreboard.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_scoreboard.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_scoreboard.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_scoreboard.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_scoreboard.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_scoreboard.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_scoreboard.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_scoreboard.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_scoreboard.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_scoreboard.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_scoreboard.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_scoreboard.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_scoreboard.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_scoreboard.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_scoreboard.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_seq_item_export`

Module: `pyuvm`

The sequence item port with a request queue and

### Constructor

Signature: `uvm_seq_item_export(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_seq_item_export` instance

### Methods

#### `uvm_seq_item_export.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_seq_item_export.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_seq_item_export.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_seq_item_export.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_seq_item_export.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_seq_item_export.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_seq_item_export.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_seq_item_export.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_seq_item_export.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_seq_item_export.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_seq_item_export.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_seq_item_export.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_seq_item_export.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_seq_item_export.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_next_item`

A couroutine that gets the next item out of the item queue

Signature: `get_next_item(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_response`

A couroutine that will block if there is no transaction

Signature: `get_response(self, transaction_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `transaction_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | The transaction ID of the response |

Output: `object`

#### `uvm_seq_item_export.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_seq_item_export.item_done`

Signal that the item has been completed. If ``rsp`` is not ``None``

Signature: `item_done(self, rsp=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rsp` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | (optional) item to put in response queue if not None |

Output: `object`

#### `uvm_seq_item_export.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_seq_item_export.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.put_req`

put request into request queue. Block if the queue is full.

Signature: `put_req(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | request item |

Output: `None`

#### `uvm_seq_item_export.put_response`

Put response into response queue. Do not block.

Signature: `put_response(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | response item |

Output: `None`

#### `uvm_seq_item_export.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_seq_item_export.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_seq_item_export.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_seq_item_export.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_seq_item_export.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_seq_item_export.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_seq_item_export.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_seq_item_export.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_seq_item_export.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_seq_item_export.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_export.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_seq_item_port`

Module: `pyuvm`

A ``uvm_port_base`` is a uvm_component with a ``connect()`` function.

### Constructor

Signature: `uvm_seq_item_port(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_seq_item_port` instance

### Methods

#### `uvm_seq_item_port.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_seq_item_port.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_seq_item_port.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_seq_item_port.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_seq_item_port.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_seq_item_port.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_seq_item_port.connect`

:param export: The export that has the functions

Signature: `connect(self, export)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `export` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The export that has the functions |

Output: `object`

#### `uvm_seq_item_port.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_seq_item_port.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_seq_item_port.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_seq_item_port.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_seq_item_port.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_seq_item_port.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_seq_item_port.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_seq_item_port.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_next_item`

A coroutine that get the next sequence item from the request queue

Signature: `get_next_item(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_response`

A coroutine that will ither get a response item with the

Signature: `get_response(self, transaction_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `transaction_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | The transaction ID of the response you want |

Output: `object`

#### `uvm_seq_item_port.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_seq_item_port.item_done`

Notify the driver that it can get the next sequence. If

Signature: `item_done(self, rsp=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rsp` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | (optional) The response item |

Output: `object`

#### `uvm_seq_item_port.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_seq_item_port.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.put_req`

A coroutine that blocks until the request is put in the queue

Signature: `put_req(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The request item |

Output: `None`

#### `uvm_seq_item_port.put_response`

Put a response back in the queue. aka put_response

Signature: `put_response(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The response item |

Output: `None`

#### `uvm_seq_item_port.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_seq_item_port.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_seq_item_port.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_seq_item_port.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_seq_item_port.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_seq_item_port.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_seq_item_port.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_seq_item_port.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_seq_item_port.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_seq_item_port.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_seq_item_port.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_sequence`

Module: `pyuvm`

The uvm_sequence creates a series of sequence

### Constructor

Signature: `uvm_sequence(self, name='uvm_sequence')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_sequence'` | Name of the object. Default is empty string. |

Output: `uvm_sequence` instance

### Methods

#### `uvm_sequence.body`

This function gets launched in a thread when you run start()

Signature: `body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.finish_item`

No description available.

Signature: `finish_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_response`

No description available.

Signature: `get_response(self, transaction_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `transaction_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | Parameter. |

Output: `object`

#### `uvm_sequence.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.post_body`

This function gets launced AFTER the function body() is started

Signature: `post_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.pre_body`

This function gets launced BEFORE the function body() is started

Signature: `pre_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_sequence.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_sequence.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_sequence.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.start`

Launch this sequence on the sequencer. Seqr cannot be None.

Signature: `start(self, seqr=None, call_pre_post=True)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `seqr` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | The sequencer to launch this sequence on. |
| `call_pre_post` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | If set to true (default), then pre_body and |

Output: `object`

#### `uvm_sequence.start_item`

Sends an item to the sequencer and waits to be notified

Signature: `start_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The sequence item to send to the driver. |

Output: `object`

#### `uvm_sequence.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_sequence_base`

Module: `pyuvm`

The pyuvm uvm_sequence_item has events to

### Constructor

Signature: `uvm_sequence_base(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Object name |

Output: `uvm_sequence_base` instance

### Methods

#### `uvm_sequence_base.accept_tr`

:param accept_time: Simulation time when the transaction is accepted

Signature: `accept_tr(self, accept_time=0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accept_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time when the transaction is accepted |

Output: `object`

#### `uvm_sequence_base.begin_tr`

:param begin_time: Simulation time at which

Signature: `begin_tr(self, begin_time=0, parent_handle=None) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `begin_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which |
| `parent_handle` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `int`

#### `uvm_sequence_base.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence_base.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence_base.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence_base.disable_recording`

Not implemented

Signature: `disable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_accept_tr`

User definable method to add to ``accept_tr()``

Signature: `do_accept_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_begin_tr`

User definable method

Signature: `do_begin_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence_base.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence_base.do_end_tr`

Not implemented

Signature: `do_end_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence_base.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.enable_recording`

Not implemented

Signature: `enable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.end_tr`

:param end_time: Simulation time at which the transaction

Signature: `end_tr(self, end_time=0, free_handle=True) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `end_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which the transaction |
| `free_handle` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_sequence_base.get_accept_time`

:return: Accept time of transaction

Signature: `get_accept_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_base.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_begin_time`

:return: Begin time of transaction

Signature: `get_begin_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_base.get_end_time`

:return: End time of transaction

Signature: `get_end_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_base.get_event_pool`

Not implemented

Signature: `get_event_pool(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_initiator`

:return: initiator

Signature: `get_initiator(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_tr_handle`

Not implemented

Signature: `get_tr_handle(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_transaction_id`

:return: Transaction ID

Signature: `get_transaction_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.is_active`

Not implemented

Signature: `is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_sequence_base.is_recording_enabled`

Not implemented

Signature: `is_recording_enabled(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_sequence_base.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.set_context`

Use this to link a new response transaction to the request transaction.

Signature: `set_context(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The request transaction |

Output: `None`

#### `uvm_sequence_base.set_id_info`

:param other: uvm_transaction with transaction_id

Signature: `set_id_info(self, other)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `other` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | uvm_transaction with transaction_id |

Output: `None`

#### `uvm_sequence_base.set_initiator`

:param initiator: initiator to set

Signature: `set_initiator(self, initiator)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | initiator to set |

Output: `None`

#### `uvm_sequence_base.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_sequence_base.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_sequence_base.set_transaction_id`

:param txn_id: Transaction ID

Signature: `set_transaction_id(self, txn_id)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Transaction ID |

Output: `None`

#### `uvm_sequence_base.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_sequence_base.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_base.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_sequence_item`

Module: `pyuvm`

The pyuvm uvm_sequence_item has events to

### Constructor

Signature: `uvm_sequence_item(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Object name |

Output: `uvm_sequence_item` instance

### Methods

#### `uvm_sequence_item.accept_tr`

:param accept_time: Simulation time when the transaction is accepted

Signature: `accept_tr(self, accept_time=0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accept_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time when the transaction is accepted |

Output: `object`

#### `uvm_sequence_item.begin_tr`

:param begin_time: Simulation time at which

Signature: `begin_tr(self, begin_time=0, parent_handle=None) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `begin_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which |
| `parent_handle` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `int`

#### `uvm_sequence_item.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence_item.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence_item.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence_item.disable_recording`

Not implemented

Signature: `disable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_accept_tr`

User definable method to add to ``accept_tr()``

Signature: `do_accept_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_begin_tr`

User definable method

Signature: `do_begin_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequence_item.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequence_item.do_end_tr`

Not implemented

Signature: `do_end_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequence_item.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.enable_recording`

Not implemented

Signature: `enable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.end_tr`

:param end_time: Simulation time at which the transaction

Signature: `end_tr(self, end_time=0, free_handle=True) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `end_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which the transaction |
| `free_handle` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_sequence_item.get_accept_time`

:return: Accept time of transaction

Signature: `get_accept_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_item.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_begin_time`

:return: Begin time of transaction

Signature: `get_begin_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_item.get_end_time`

:return: End time of transaction

Signature: `get_end_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_sequence_item.get_event_pool`

Not implemented

Signature: `get_event_pool(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_initiator`

:return: initiator

Signature: `get_initiator(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_tr_handle`

Not implemented

Signature: `get_tr_handle(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_transaction_id`

:return: Transaction ID

Signature: `get_transaction_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.is_active`

Not implemented

Signature: `is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_sequence_item.is_recording_enabled`

Not implemented

Signature: `is_recording_enabled(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_sequence_item.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.set_context`

Use this to link a new response transaction to the request transaction.

Signature: `set_context(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The request transaction |

Output: `None`

#### `uvm_sequence_item.set_id_info`

:param other: uvm_transaction with transaction_id

Signature: `set_id_info(self, other)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `other` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | uvm_transaction with transaction_id |

Output: `None`

#### `uvm_sequence_item.set_initiator`

:param initiator: initiator to set

Signature: `set_initiator(self, initiator)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | initiator to set |

Output: `None`

#### `uvm_sequence_item.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_sequence_item.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_sequence_item.set_transaction_id`

:param txn_id: Transaction ID

Signature: `set_transaction_id(self, txn_id)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Transaction ID |

Output: `None`

#### `uvm_sequence_item.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_sequence_item.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequence_item.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_sequencer`

Module: `pyuvm`

The uvm_sequencer arbitrates between multiple sequences that want to send

### Constructor

Signature: `uvm_sequencer(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_sequencer` instance

### Methods

#### `uvm_sequencer.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_sequencer.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_sequencer.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_sequencer.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_sequencer.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequencer.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequencer.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_sequencer.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequencer.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequencer.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_sequencer.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.finish_item`

No description available.

Signature: `finish_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_sequencer.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_next_item`

No description available.

Signature: `get_next_item(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_response`

No description available.

Signature: `get_response(self, txn_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | Parameter. |

Output: `object`

#### `uvm_sequencer.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_sequencer.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_sequencer.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.put_req`

No description available.

Signature: `put_req(self, req)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `req` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_sequencer.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_sequencer.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_sequencer.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_sequencer.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_sequencer.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_sequencer.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_sequencer.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_sequencer.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_sequencer.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_sequencer.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.start_item`

No description available.

Signature: `start_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_sequencer_base`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_sequencer_base(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_sequencer_base` instance

### Methods

#### `uvm_sequencer_base.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequencer_base.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequencer_base.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer_base.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_sequencer_base.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_sequencer_base.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_sequencer_base.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_sequencer_base.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_sequencer_base.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_sequencer_base.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_sequencer_base.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_start_of_simulation_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_start_of_simulation_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_start_of_simulation_phase` instance

### Methods

#### `uvm_start_of_simulation_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_start_of_simulation_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_start_of_simulation_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_start_of_simulation_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_start_of_simulation_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_start_of_simulation_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_start_of_simulation_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_start_of_simulation_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_start_of_simulation_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_start_of_simulation_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_subscriber`

Module: `pyuvm`

This class provides an analysis export for receiving transactions from a

### Constructor

Signature: `uvm_subscriber(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_subscriber` instance

### Methods

#### `uvm_subscriber.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_subscriber.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_subscriber.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_subscriber.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_subscriber.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_subscriber.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_subscriber.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_subscriber.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_subscriber.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_subscriber.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_subscriber.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_subscriber.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_subscriber.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_subscriber.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_subscriber.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_subscriber.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_subscriber.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_subscriber.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_subscriber.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_subscriber.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_subscriber.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_subscriber.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_subscriber.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_subscriber.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_subscriber.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_subscriber.write`

Method that must be defined in each subclass. Access to this method by

Signature: `write(self, tt)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `tt` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

## Class `uvm_test`

Module: `pyuvm`

The base class for all tests

### Constructor

Signature: `uvm_test(self, name, parent)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_test` instance

### Methods

#### `uvm_test.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_test.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_test.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_test.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_test.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_test.check_phase`

No description available.

Signature: `check_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_test.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_test.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_test.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_test.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_test.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_test.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_test.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_test.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_test.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_test.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_test.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_test.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_test.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_test.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_test.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_test.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_test.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_test.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_test.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_test.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_threaded_execute_phase`

Module: `pyuvm`

This phase launches the phase function in a thread and

### Constructor

Signature: `uvm_threaded_execute_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_threaded_execute_phase` instance

### Methods

#### `uvm_threaded_execute_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_threaded_execute_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_threaded_execute_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_threaded_execute_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_threaded_execute_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_threaded_execute_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_threaded_execute_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_threaded_execute_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_threaded_execute_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_threaded_execute_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_threaded_execute_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_threaded_execute_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_topdown_phase`

Module: `pyuvm`

Runs phases from the top down.

### Constructor

Signature: `uvm_topdown_phase(self, name='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_topdown_phase` instance

### Methods

#### `uvm_topdown_phase.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_topdown_phase.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_topdown_phase.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_topdown_phase.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_topdown_phase.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_topdown_phase.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_topdown_phase.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.execute`

:param comp: The component whose turn it is to execute

Signature: `execute(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose turn it is to execute |

Output: `object`

#### `uvm_topdown_phase.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_topdown_phase.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_topdown_phase.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_topdown_phase.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.traverse`

:param comp: The component whose hierarchy will be traversed

Signature: `traverse(comp)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `comp` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The component whose hierarchy will be traversed |

Output: `object`

#### `uvm_topdown_phase.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_topdown_phase.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_transaction`

Module: `pyuvm`

Transactions without interface to logging or waveforms.

### Constructor

Signature: `uvm_transaction(self, name='', initiator=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Object name |
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | component that is the initiator |

Output: `uvm_transaction` instance

### Methods

#### `uvm_transaction.accept_tr`

:param accept_time: Simulation time when the transaction is accepted

Signature: `accept_tr(self, accept_time=0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accept_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time when the transaction is accepted |

Output: `object`

#### `uvm_transaction.begin_tr`

:param begin_time: Simulation time at which

Signature: `begin_tr(self, begin_time=0, parent_handle=None) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `begin_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which |
| `parent_handle` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `int`

#### `uvm_transaction.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_transaction.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_transaction.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_transaction.disable_recording`

Not implemented

Signature: `disable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_accept_tr`

User definable method to add to ``accept_tr()``

Signature: `do_accept_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_begin_tr`

User definable method

Signature: `do_begin_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_transaction.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_transaction.do_end_tr`

Not implemented

Signature: `do_end_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_transaction.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.enable_recording`

Not implemented

Signature: `enable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.end_tr`

:param end_time: Simulation time at which the transaction

Signature: `end_tr(self, end_time=0, free_handle=True) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `end_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which the transaction |
| `free_handle` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_transaction.get_accept_time`

:return: Accept time of transaction

Signature: `get_accept_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_transaction.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_begin_time`

:return: Begin time of transaction

Signature: `get_begin_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_transaction.get_end_time`

:return: End time of transaction

Signature: `get_end_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_transaction.get_event_pool`

Not implemented

Signature: `get_event_pool(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_initiator`

:return: initiator

Signature: `get_initiator(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_tr_handle`

Not implemented

Signature: `get_tr_handle(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_transaction_id`

:return: Transaction ID

Signature: `get_transaction_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.is_active`

Not implemented

Signature: `is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_transaction.is_recording_enabled`

Not implemented

Signature: `is_recording_enabled(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_transaction.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.set_id_info`

:param other: uvm_transaction with transaction_id

Signature: `set_id_info(self, other)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `other` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | uvm_transaction with transaction_id |

Output: `None`

#### `uvm_transaction.set_initiator`

:param initiator: initiator to set

Signature: `set_initiator(self, initiator)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | initiator to set |

Output: `None`

#### `uvm_transaction.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_transaction.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_transaction.set_transaction_id`

:param txn_id: Transaction ID

Signature: `set_transaction_id(self, txn_id)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Transaction ID |

Output: `None`

#### `uvm_transaction.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_transaction.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_transaction.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Constant `uvm_common_phases`

Module: `builtins`

Type: `list`

Value: `[<class 'pyuvm.uvm_build_phase'>, <class 'pyuvm.uvm_connect_phase'>, <class 'pyuvm.uvm_end_of_elaboration_phase'>, <class 'pyuvm.uvm_start_of_simulation_phase'>, <class 'pyuvm.uvm_run_phase'>, <class 'pyuvm.uvm_extract_phase'>, <class 'pyuvm.uvm_check_phase'>, <class 'pyuvm.uvm_report_phase'>, <class 'pyuvm.uvm_final_phase'>]`

