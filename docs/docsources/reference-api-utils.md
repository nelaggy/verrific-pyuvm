# API Reference: Errors and Utilities

Auto-generated API reference for error classes, utility helpers, and extension-level callables/constants.

Type legend:

- `object`: no explicit annotation was available; type inferred from docs/defaults/name where possible.
- `required` default: argument has no default and must be supplied by caller.

## Coverage

- Symbols in this page: `21`
- Classes: `16`
- Functions/callables: `2`
- Constants/other values: `3`

## Index

### Classes

- `FactoryData`
- `FactoryMeta`
- `Objection`
- `ObjectionHandler`
- `Override`
- `Singleton`
- `UVMConfigError`
- `UVMError`
- `UVMFactoryError`
- `UVMFatalError`
- `UVMNotImplemented`
- `UVMQueue`
- `UVMSequenceError`
- `UVMTLMConnectionError`
- `UVM_ROOT_Singleton`
- `uvm_void`

### Functions

- `count_bits`
- `test`

### Constants

- `FIFO_DEBUG`
- `PYUVM_DEBUG`
- `__version__`

## Class `FactoryData`

Module: `pyuvm`

No description available.

### Constructor

Signature: `FactoryData(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `FactoryData` instance

### Methods

#### `FactoryData.clear_classes`

No description available.

Signature: `clear_classes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `FactoryData.clear_overrides`

No description available.

Signature: `clear_overrides(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `FactoryData.find_override`

:param requested_type: The type we're overriding

Signature: `find_override(self, requested_type, inst_path=None, overridden_list=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `requested_type` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The type we're overriding |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `None` | The inst_path we're using to override if any |
| `overridden_list` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | A list of previously found overrides |

Output: `object`

## Class `FactoryMeta`

Module: `pyuvm`

This is the metaclass that causes all uvm_void classes

### Constructor

Signature: `FactoryMeta(cls, name, bases, cls_dict)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `bases` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cls_dict` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `FactoryMeta` instance

### Methods

#### `FactoryMeta.mro`

Return a type's method resolution order.

Signature: `mro(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `Objection`

Module: `pyuvm`

Details about a raised objection, to assist in diagnosing hangs/timeouts

### Constructor

Signature: `Objection(self, raiser_name: str, description: str, sourceline: str) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `raiser_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `sourceline` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `Objection` instance

## Class `ObjectionHandler`

Module: `pyuvm`

This singleton accepts objections and then allows

### Constructor

Signature: `ObjectionHandler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `ObjectionHandler` instance

### Methods

#### `ObjectionHandler.clear`

No description available.

Signature: `clear(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `ObjectionHandler.drop_objection`

No description available.

Signature: `drop_objection(self, dropper, description)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `dropper` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `ObjectionHandler.raise_objection`

No description available.

Signature: `raise_objection(self, raiser, description, stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `raiser` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |

Output: `None`

#### `ObjectionHandler.run_phase_complete`

No description available.

Signature: `run_phase_complete(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `Override`

Module: `pyuvm`

This class stores an override and an optional path.

### Constructor

Signature: `Override(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `Override` instance

### Methods

#### `Override.add`

No description available.

Signature: `add(self, override, path=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `override` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `object`

#### `Override.find_inst_override`

No description available.

Signature: `find_inst_override(self, path)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

## Class `Singleton`

Module: `pyuvm`

type(object) -> the object's type

### Constructor

Signature: `Singleton(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `Singleton` instance

### Methods

#### `Singleton.clear_singletons`

No description available.

Signature: `clear_singletons(keep)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `keep` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `Singleton.mro`

Return a type's method resolution order.

Signature: `mro(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `UVMConfigError`

Module: `pyuvm`

Errors using the config_db

### Constructor

Signature: `UVMConfigError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMConfigError` instance

### Methods

#### `UVMConfigError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMConfigError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMError`

Module: `pyuvm`

All UVM Errors

### Constructor

Signature: `UVMError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMError` instance

### Methods

#### `UVMError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMFactoryError`

Module: `pyuvm`

For cases where a type is not registered with the factory

### Constructor

Signature: `UVMFactoryError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMFactoryError` instance

### Methods

#### `UVMFactoryError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMFactoryError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMFatalError`

Module: `pyuvm`

Used to dump out of the testbench

### Constructor

Signature: `UVMFatalError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMFatalError` instance

### Methods

#### `UVMFatalError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMFatalError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMNotImplemented`

Module: `pyuvm`

For methods that we haven't yet implemented.

### Constructor

Signature: `UVMNotImplemented(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMNotImplemented` instance

### Methods

#### `UVMNotImplemented.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMNotImplemented.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMQueue`

Module: `pyuvm`

The UVMQueue provides a peek function as well as the

### Constructor

Signature: `UVMQueue(self, maxsize: int = 0) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maxsize` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `UVMQueue` instance

### Methods

#### `UVMQueue.empty`

Return ``True`` if the queue is empty, ``False`` otherwise.

Signature: `empty(self) -> bool`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `UVMQueue.full`

Return ``True`` if there are :meth:`maxsize` items in the queue.

Signature: `full(self) -> bool`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `UVMQueue.get`

Remove and return an item from the queue.

Signature: `get(self) -> ~T`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `~T`

#### `UVMQueue.get_nowait`

Remove and return an item from the queue.

Signature: `get_nowait(self) -> ~T`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `~T`

#### `UVMQueue.peek`

Remove and return an item from the queue.

Signature: `peek(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `UVMQueue.peek_nowait`

Remove and return an item from the queue.

Signature: `peek_nowait(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `UVMQueue.put`

Put an *item* into the queue.

Signature: `put(self, item: ~T) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `~T` | `required` | Parameter. |

Output: `None`

#### `UVMQueue.put_nowait`

Put an *item* into the queue without blocking.

Signature: `put_nowait(self, item: ~T) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `~T` | `required` | Parameter. |

Output: `None`

#### `UVMQueue.qsize`

Number of items in the queue.

Signature: `qsize(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

## Class `UVMSequenceError`

Module: `pyuvm`

Errors using sequences

### Constructor

Signature: `UVMSequenceError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMSequenceError` instance

### Methods

#### `UVMSequenceError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMSequenceError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVMTLMConnectionError`

Module: `pyuvm`

For problems connecting TLM

### Constructor

Signature: `UVMTLMConnectionError(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `UVMTLMConnectionError` instance

### Methods

#### `UVMTLMConnectionError.add_note`

Exception.add_note(note) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `UVMTLMConnectionError.with_traceback`

Exception.with_traceback(tb) --

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

## Class `UVM_ROOT_Singleton`

Module: `pyuvm`

This is the metaclass that causes all uvm_void classes

### Constructor

Signature: `UVM_ROOT_Singleton(cls, name, bases, cls_dict)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `bases` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cls_dict` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `UVM_ROOT_Singleton` instance

### Methods

#### `UVM_ROOT_Singleton.clear_singletons`

No description available.

Signature: `clear_singletons()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `UVM_ROOT_Singleton.mro`

Return a type's method resolution order.

Signature: `mro(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_void`

Module: `pyuvm`

5.2

### Constructor

Signature: `uvm_void(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_void` instance

## Function `count_bits`

Module: `pyuvm`

Count the number of bits in a number

Signature: `count_bits(nn)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `nn` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The number to count the bits in |

Output: `object`

## Function `test`

Module: `pyuvm`

No description available.

Signature: `test(timeout_time=None, timeout_unit='step', expect_fail=False, expect_error=(), skip=False, stage=None, keep_singletons=False, keep_set=set())`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `timeout_time` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |
| `timeout_unit` | `POSITIONAL_OR_KEYWORD` | `str` | `'step'` | Parameter. |
| `expect_fail` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `expect_error` | `POSITIONAL_OR_KEYWORD` | `tuple` | `()` | Parameter. |
| `skip` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `stage` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |
| `keep_singletons` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `keep_set` | `POSITIONAL_OR_KEYWORD` | `set` | `set()` | Parameter. |

Output: `object`

## Constant `FIFO_DEBUG`

Module: `builtins`

Type: `int`

Value: `5`

## Constant `PYUVM_DEBUG`

Module: `builtins`

Type: `int`

Value: `4`

## Constant `__version__`

Module: `builtins`

Type: `str`

Value: `'4.0.1'`

