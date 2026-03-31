# API Reference: Register Layer (RAL)

Auto-generated API reference for register model, fields, maps, adapters, predictors, and related enums/types.

Type legend:

- `object`: no explicit annotation was available; type inferred from docs/defaults/name where possible.
- `required` default: argument has no default and must be supplied by caller.

## Coverage

- Symbols in this page: `64`
- Classes: `64`
- Functions/callables: `0`
- Constants/other values: `0`

## Index

### Classes

- `uvm_access_e`
- `uvm_check_e`
- `uvm_coverage_model_e`
- `uvm_door_e`
- `uvm_elem_kind_e`
- `uvm_endianness_e`
- `uvm_hdl_path_concat`
- `uvm_hdl_path_slice`
- `uvm_hier_e`
- `uvm_mem`
- `uvm_mem_cb`
- `uvm_mem_cb_iter`
- `uvm_mem_mam`
- `uvm_mem_mam_cfg`
- `uvm_mem_mam_policy`
- `uvm_mem_region`
- `uvm_object_string_pool`
- `uvm_path_e`
- `uvm_predict_e`
- `uvm_reg`
- `uvm_reg_adapter`
- `uvm_reg_addr_logic_t`
- `uvm_reg_addr_t`
- `uvm_reg_backdoor`
- `uvm_reg_bd_cb`
- `uvm_reg_bd_cb_iter`
- `uvm_reg_block`
- `uvm_reg_bus_op`
- `uvm_reg_byte_en_t`
- `uvm_reg_cb`
- `uvm_reg_cb_iter`
- `uvm_reg_cbs`
- `uvm_reg_cvr_t`
- `uvm_reg_data_logic_t`
- `uvm_reg_data_t`
- `uvm_reg_field`
- `uvm_reg_field_cb`
- `uvm_reg_field_cb_iter`
- `uvm_reg_fifo`
- `uvm_reg_file`
- `uvm_reg_frontdoor`
- `uvm_reg_indirect_data`
- `uvm_reg_indirect_ftdr_seq`
- `uvm_reg_item`
- `uvm_reg_map`
- `uvm_reg_map_addr_range`
- `uvm_reg_map_info`
- `uvm_reg_mem_test_e`
- `uvm_reg_predictor`
- `uvm_reg_read_only_cbs`
- `uvm_reg_seq_base`
- `uvm_reg_sequence`
- `uvm_reg_tlm_adapter`
- `uvm_reg_transaction_order_policy`
- `uvm_reg_write_only_cbs`
- `uvm_status_e`
- `uvm_vreg`
- `uvm_vreg_cb`
- `uvm_vreg_cb_iter`
- `uvm_vreg_cbs`
- `uvm_vreg_field`
- `uvm_vreg_field_cb`
- `uvm_vreg_field_cb_iter`
- `uvm_vreg_field_cbs`

### Functions


## Class `uvm_access_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_READ` | `0` | Enum member. |
| `UVM_WRITE` | `1` | Enum member. |
| `UVM_BURST_READ` | `2` | Enum member. |
| `UVM_BURST_WRITE` | `3` | Enum member. |

## Class `uvm_check_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_NO_CHECK` | `0` | Enum member. |
| `UVM_CHECK` | `1` | Enum member. |

## Class `uvm_coverage_model_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_NO_COVERAGE` | `0` | Enum member. |
| `UVM_CVR_REG_BITS` | `1` | Enum member. |
| `UVM_CVR_ADDR_MAP` | `2` | Enum member. |
| `UVM_CVR_FIELD_VALS` | `4` | Enum member. |
| `UVM_CVR_ALL` | `-1` | Enum member. |

## Class `uvm_door_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_FRONTDOOR` | `0` | Enum member. |
| `UVM_BACKDOOR` | `1` | Enum member. |
| `UVM_PREDICT` | `2` | Enum member. |
| `UVM_DEFAULT_DOOR` | `3` | Enum member. |

## Class `uvm_elem_kind_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_REG` | `0` | Enum member. |
| `UVM_FIELD` | `1` | Enum member. |
| `UVM_MEM` | `2` | Enum member. |

## Class `uvm_endianness_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_NO_ENDIAN` | `0` | Enum member. |
| `UVM_LITTLE_ENDIAN` | `1` | Enum member. |
| `UVM_BIG_ENDIAN` | `2` | Enum member. |
| `UVM_LITTLE_FIFO` | `3` | Enum member. |
| `UVM_BIG_FIFO` | `4` | Enum member. |

## Class `uvm_hdl_path_concat`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_hdl_path_concat(self, name: str = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_hdl_path_concat` instance

### Methods

#### `uvm_hdl_path_concat.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_hdl_path_concat.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_hdl_path_concat.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_hdl_path_concat.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_hdl_path_concat.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_hdl_path_concat.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_hdl_path_concat.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_hdl_path_concat.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_hdl_path_concat.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_hdl_path_concat.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_concat.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_hdl_path_slice`

Module: `pyuvm`

uvm_hdl_path_slice(path: str, offset: int, size: int)

### Constructor

Signature: `uvm_hdl_path_slice(self, path: str, offset: int, size: int) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `uvm_hdl_path_slice` instance

### Methods

#### `uvm_hdl_path_slice.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_hdl_path_slice.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_hdl_path_slice.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_hdl_path_slice.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_hdl_path_slice.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_hdl_path_slice.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_hdl_path_slice.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_hdl_path_slice.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_hdl_path_slice.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_hdl_path_slice.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_hdl_path_slice.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_hier_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_NO_HIER` | `0` | Enum member. |
| `UVM_HIER` | `1` | Enum member. |

## Class `uvm_mem`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_mem(self, name: 'str', size: 'int', n_bits: 'int', access: 'str' = 'RW', has_coverage: 'int' = <uvm_coverage_model_e.UVM_NO_COVERAGE: 0>) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object. Default is empty string. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `access` | `POSITIONAL_OR_KEYWORD` | `str` | `'RW'` | Parameter. |
| `has_coverage` | `POSITIONAL_OR_KEYWORD` | `int` | `<uvm_coverage_model_e.UVM_NO_COVERAGE: 0>` | Parameter. |

Output: `uvm_mem` instance

### Methods

#### `uvm_mem.add_coverage`

No description available.

Signature: `add_coverage(self, models: 'uvm_reg_cvr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, slices: 'list[uvm_hdl_path_slice]', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `slices` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_slice]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_mem.add_hdl_path_slice`

No description available.

Signature: `add_hdl_path_slice(self, name: 'str', offset: 'int', size: 'int', first: 'bool' = False, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `first` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_mem.add_map`

No description available.

Signature: `add_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.backdoor_read`

No description available.

Signature: `backdoor_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.backdoor_read_func`

No description available.

Signature: `backdoor_read_func(self, rw: 'uvm_reg_item') -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem.backdoor_write`

No description available.

Signature: `backdoor_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.build_coverage`

No description available.

Signature: `build_coverage(self, models: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_mem.burst_read`

No description available.

Signature: `burst_read(self, offset: 'uvm_reg_addr_t', value: 'list[uvm_reg_data_t]', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_data_t]` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem.burst_write`

No description available.

Signature: `burst_write(self, offset: 'uvm_reg_addr_t', value: 'list[uvm_reg_data_t]', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_data_t]` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_mem.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_mem.configure`

No description available.

Signature: `configure(self, parent: 'uvm_reg_block', hdl_path: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_mem.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_mem.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_mem.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_mem.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_mem.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_mem.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.get_access`

No description available.

Signature: `get_access(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_mem.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_address`

No description available.

Signature: `get_address(self, offset: 'uvm_reg_addr_t' = 0, map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_mem.get_addresses`

No description available.

Signature: `get_addresses(self, offset: 'uvm_reg_addr_t' = 0, map: 'uvm_reg_map' = None) -> 'tuple[int, list[uvm_reg_addr_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `tuple[int, list[uvm_reg_addr_t]]`

#### `uvm_mem.get_backdoor`

No description available.

Signature: `get_backdoor(self, inherited: 'bool' = True) -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `inherited` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_backdoor`

#### `uvm_mem.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_mem.get_coverage`

No description available.

Signature: `get_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_mem.get_default_map`

No description available.

Signature: `get_default_map(self) -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map | None`

#### `uvm_mem.get_frontdoor`

No description available.

Signature: `get_frontdoor(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_frontdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_frontdoor`

#### `uvm_mem.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_mem.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_mem.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_mem.get_hdl_path_kinds`

No description available.

Signature: `get_hdl_path_kinds(self, kinds: 'list[str]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kinds` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_local_map`

No description available.

Signature: `get_local_map(self, map: 'uvm_reg_map') -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_map | None`

#### `uvm_mem.get_maps`

No description available.

Signature: `get_maps(self, maps: 'list[uvm_reg_map]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maps` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_map]` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.get_max_size`

No description available.

Signature: `get_max_size() -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem.get_n_maps`

No description available.

Signature: `get_n_maps(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_offset`

No description available.

Signature: `get_offset(self, offset: 'uvm_reg_addr_t' = 0, map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_mem.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_mem.get_rights`

No description available.

Signature: `get_rights(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_mem.get_size`

No description available.

Signature: `get_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.get_vfield_by_name`

No description available.

Signature: `get_vfield_by_name(self, name: 'str') -> 'uvm_vreg_field | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg_field | None`

#### `uvm_mem.get_virtual_fields`

No description available.

Signature: `get_virtual_fields(self) -> 'list[uvm_vreg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_vreg_field]`

#### `uvm_mem.get_virtual_registers`

No description available.

Signature: `get_virtual_registers(self) -> 'list[uvm_vreg]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_vreg]`

#### `uvm_mem.get_vreg`

No description available.

Signature: `get_vreg(self, name: 'str') -> 'uvm_vreg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg`

#### `uvm_mem.get_vreg_by_name`

No description available.

Signature: `get_vreg_by_name(self, name: 'str') -> 'uvm_vreg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg | None`

#### `uvm_mem.get_vreg_by_offset`

No description available.

Signature: `get_vreg_by_offset(self, offset: 'uvm_reg_addr_t', map: 'uvm_reg_map' = None) -> 'uvm_vreg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_vreg`

#### `uvm_mem.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_mem.is_in_map`

No description available.

Signature: `is_in_map(self, map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_mem.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.peek`

No description available.

Signature: `peek(self, offset: 'uvm_reg_addr_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_mem.poke`

No description available.

Signature: `poke(self, offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.pre_read`

No description available.

Signature: `pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.pre_write`

No description available.

Signature: `pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.read`

No description available.

Signature: `read(self, offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_mem.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.sample`

No description available.

Signature: `sample(self, offset: 'uvm_reg_addr_t', is_read: 'bool', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `is_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.set_backdoor`

No description available.

Signature: `set_backdoor(self, bkdr: 'uvm_reg_backdoor', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bkdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_backdoor` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_mem.set_coverage`

No description available.

Signature: `set_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_mem.set_frontdoor`

No description available.

Signature: `set_frontdoor(self, ftdr: 'uvm_reg_frontdoor', map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `ftdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_mem.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_mem.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_mem.set_offset`

No description available.

Signature: `set_offset(self, map: 'uvm_reg_map', offset: 'uvm_reg_addr_t', unmapped: 'bool' = False) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_mem.set_parent`

No description available.

Signature: `set_parent(self, parent: 'uvm_reg_block') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_mem.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem.write`

No description available.

Signature: `write(self, offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_mem_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_mem_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_mem_cb` instance

### Methods

#### `uvm_mem_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_mem_cb.add_by_name`

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

#### `uvm_mem_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_mem_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_mem_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_mem_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_mem_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_mem_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_mem_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_mem_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_mem_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_mem_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_mem_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_mem_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_mem_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_mem_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_mem_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_mem_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_mem_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_mem_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_mem_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_mem_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_mem_cb_iter` instance

### Methods

#### `uvm_mem_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_mem_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_mem_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_mem_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_mem_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_mem_mam`

Module: `pyuvm`

5.2

### Constructor

Signature: `uvm_mem_mam(self, name: 'str', cfg: 'uvm_mem_mam_cfg', mem: 'uvm_mem' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cfg` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam_cfg` | `required` | Parameter. |
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `None` | Parameter. |

Output: `uvm_mem_mam` instance

### Methods

#### `uvm_mem_mam.for_each`

No description available.

Signature: `for_each(reset: 'bool' = False) -> 'uvm_mem_region'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `reset` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `uvm_mem_region`

#### `uvm_mem_mam.get_memory`

No description available.

Signature: `get_memory(self) -> 'uvm_mem'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_mem`

#### `uvm_mem_mam.reconfigure`

No description available.

Signature: `reconfigure(self, cfg: 'uvm_mem_mam_cfg' = None) -> 'uvm_mem_mam_cfg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `cfg` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam_cfg` | `None` | Parameter. |

Output: `uvm_mem_mam_cfg`

#### `uvm_mem_mam.release_all_regions`

No description available.

Signature: `release_all_regions(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_mem_mam.release_region`

No description available.

Signature: `release_region(self, region: 'uvm_mem_region') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `region` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_region` | `required` | Parameter. |

Output: `None`

#### `uvm_mem_mam.request_region`

No description available.

Signature: `request_region(self, n_bytes: 'int', alloc: 'uvm_mem_mam_policy' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_mem_region'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `alloc` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam_policy` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_mem_region`

#### `uvm_mem_mam.reserve_region`

No description available.

Signature: `reserve_region(self, start_offset: 'uvm_reg_addr_t', n_bytes: 'int', fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_mem_region'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `start_offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_mem_region`

## Class `uvm_mem_mam_cfg`

Module: `pyuvm`

5.2

### Constructor

Signature: `uvm_mem_mam_cfg(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_mem_mam_cfg` instance

## Class `uvm_mem_mam_policy`

Module: `pyuvm`

5.2

### Constructor

Signature: `uvm_mem_mam_policy(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_mem_mam_policy` instance

## Class `uvm_mem_region`

Module: `pyuvm`

5.2

### Constructor

Signature: `uvm_mem_region(self, start_offset: 'uvm_reg_addr_t', end_offset: 'uvm_reg_addr_t', len: 'int', n_bytes: 'int', parent: 'uvm_mem_mam') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `start_offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `end_offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `len` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam` | `required` | Parameter. |

Output: `uvm_mem_region` instance

### Methods

#### `uvm_mem_region.burst_read`

No description available.

Signature: `burst_read(self, offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, list[uvm_reg_data_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, list[uvm_reg_data_t]]`

#### `uvm_mem_region.burst_write`

No description available.

Signature: `burst_write(self, offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem_region.get_end_offset`

No description available.

Signature: `get_end_offset(self) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_addr_t`

#### `uvm_mem_region.get_len`

No description available.

Signature: `get_len(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem_region.get_memory`

No description available.

Signature: `get_memory(self) -> 'uvm_mem'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_mem`

#### `uvm_mem_region.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_mem_region.get_start_offset`

No description available.

Signature: `get_start_offset(self) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_addr_t`

#### `uvm_mem_region.get_virtual_registers`

No description available.

Signature: `get_virtual_registers(self) -> 'uvm_vreg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_vreg`

#### `uvm_mem_region.peek`

No description available.

Signature: `peek(self, offset: 'uvm_reg_addr_t', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_mem_region.poke`

No description available.

Signature: `poke(self, offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_mem_region.read`

No description available.

Signature: `read(self, offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_mem_region.release_region`

No description available.

Signature: `release_region(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_mem_region.write`

No description available.

Signature: `write(self, offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_object_string_pool`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_object_string_pool(self, name: str = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_object_string_pool` instance

### Methods

#### `uvm_object_string_pool.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_object_string_pool.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_object_string_pool.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_object_string_pool.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_object_string_pool.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_object_string_pool.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_object_string_pool.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_object_string_pool.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_object_string_pool.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_object_string_pool.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_object_string_pool.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_path_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|

## Class `uvm_predict_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_PREDICT_DIRECT` | `0` | Enum member. |
| `UVM_PREDICT_READ` | `1` | Enum member. |
| `UVM_PREDICT_WRITE` | `2` | Enum member. |

## Class `uvm_reg`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg(self, name='', n_bits: 'int' = 0, has_coverage: 'int' = 0, **kwargs) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `has_coverage` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg` instance

### Methods

#### `uvm_reg.add_coverage`

No description available.

Signature: `add_coverage(self, models: 'uvm_reg_cvr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, slices: 'list[uvm_hdl_path_slice]', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `slices` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_slice]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg.add_hdl_path_slice`

No description available.

Signature: `add_hdl_path_slice(self, name: 'str', offset: 'int', size: 'int', first: 'bool' = False, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `first` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg.add_map`

No description available.

Signature: `add_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.backdoor_read`

No description available.

Signature: `backdoor_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.backdoor_read_func`

No description available.

Signature: `backdoor_read_func(self, rw: 'uvm_reg_item') -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg.backdoor_watch`

No description available.

Signature: `backdoor_watch(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg.backdoor_write`

No description available.

Signature: `backdoor_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.build_coverage`

No description available.

Signature: `build_coverage(self, models: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg.check_err_list`

No description available.

Signature: `check_err_list(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg.configure`

No description available.

Signature: `configure(self, blk_parent: 'uvm_reg_block', regfile_parent: 'uvm_reg_file' = None, hdl_path: 'str' = '', throw_error_on_read: 'bool' = False, throw_error_on_write: 'bool' = False, **kwargs) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `blk_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `regfile_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_file` | `None` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `throw_error_on_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `throw_error_on_write` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg.do_check`

No description available.

Signature: `do_check(self, expected: 'uvm_reg_data_t', actual: 'uvm_reg_data_t', map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `expected` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `actual` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.do_predict`

No description available.

Signature: `do_predict(self, rw: 'uvm_reg_item', kind: 'uvm_predict_e', be: 'uvm_reg_byte_en_t' = -1) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |

Output: `None`

#### `uvm_reg.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.get`

No description available.

Signature: `get(self, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg.get_access_policy`

No description available.

Signature: `get_access_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_address`

No description available.

Signature: `get_address(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg.get_addresses`

No description available.

Signature: `get_addresses(self, map: 'uvm_reg_map' = None) -> 'tuple[int, list[uvm_reg_addr_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `tuple[int, list[uvm_reg_addr_t]]`

#### `uvm_reg.get_backdoor`

No description available.

Signature: `get_backdoor(self, inherited: 'bool' = True) -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `inherited` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_backdoor`

#### `uvm_reg.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg.get_coverage`

No description available.

Signature: `get_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg.get_default_map`

No description available.

Signature: `get_default_map(self) -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map | None`

#### `uvm_reg.get_desired`

No description available.

Signature: `get_desired(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_field_by_name`

No description available.

Signature: `get_field_by_name(self, name: 'str') -> 'uvm_reg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_field`

#### `uvm_reg.get_fields`

No description available.

Signature: `get_fields(self) -> 'list[uvm_reg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_field]`

#### `uvm_reg.get_frontdoor`

No description available.

Signature: `get_frontdoor(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_frontdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_frontdoor`

#### `uvm_reg.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_reg.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg.get_hdl_path_kind`

No description available.

Signature: `get_hdl_path_kind(self, kinds: 'list[str]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kinds` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_local_map`

No description available.

Signature: `get_local_map(self, map: 'uvm_reg_map') -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_map | None`

#### `uvm_reg.get_maps`

No description available.

Signature: `get_maps(self, maps: 'list[uvm_reg_map]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maps` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_map]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.get_max_size`

No description available.

Signature: `get_max_size() -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg.get_mirrored_value`

No description available.

Signature: `get_mirrored_value(self, fname: 'str' = '', lineno: 'int' = 0) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `int`

#### `uvm_reg.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg.get_n_maps`

No description available.

Signature: `get_n_maps(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_offset`

No description available.

Signature: `get_offset(self, map: 'uvm_reg_map') -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg.get_reg_by_full_name`

No description available.

Signature: `get_reg_by_full_name(full_name: 'str') -> 'uvm_reg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `full_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg | None`

#### `uvm_reg.get_reg_size`

No description available.

Signature: `get_reg_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg.get_regfile`

No description available.

Signature: `get_regfile(self) -> 'uvm_reg_file'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_file`

#### `uvm_reg.get_reset`

No description available.

Signature: `get_reset(self, kind: 'str' = 'HARD') -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `int`

#### `uvm_reg.get_rights`

No description available.

Signature: `get_rights(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_reg.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.has_coverage`

No description available.

Signature: `has_coverage(self, models: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg.has_reset`

No description available.

Signature: `has_reset(self, kind: 'str' = 'HARD', delete: 'bool' = False) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |
| `delete` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `bool`

#### `uvm_reg.include_coverage`

No description available.

Signature: `include_coverage(self, scope: 'str', models: 'uvm_reg_cvr_t', accessor: 'uvm_object' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `scope` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |
| `accessor` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |

Output: `None`

#### `uvm_reg.is_busy`

No description available.

Signature: `is_busy(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg.is_in_map`

No description available.

Signature: `is_in_map(self, map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg.mirror`

No description available.

Signature: `mirror(self, check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg.needs_update`

No description available.

Signature: `needs_update() -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.peek`

No description available.

Signature: `peek(self, kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg.poke`

No description available.

Signature: `poke(self, value: 'uvm_reg_data_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.pre_read`

No description available.

Signature: `pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.pre_write`

No description available.

Signature: `pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.predict`

No description available.

Signature: `predict(self, value: 'uvm_reg_data_t', be: 'uvm_reg_byte_en_t' = -1, kind: 'uvm_predict_e' = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_FRONTDOOR: 0>, map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_FRONTDOOR: 0>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `bool`

#### `uvm_reg.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.read`

No description available.

Signature: `read(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg.sample`

No description available.

Signature: `sample(self, data: 'uvm_reg_data_t', byte_en: 'uvm_reg_data_t', is_read: 'bool', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `byte_en` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `is_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.sample_values`

No description available.

Signature: `sample_values(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg.set`

No description available.

Signature: `set(self, value: 'uvm_reg_data_t', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg.set_backdoor`

No description available.

Signature: `set_backdoor(self, bkdr: 'uvm_reg_backdoor', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bkdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_backdoor` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg.set_coverage`

No description available.

Signature: `set_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg.set_desired`

No description available.

Signature: `set_desired(self, value)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.set_frontdoor`

No description available.

Signature: `set_frontdoor(self, ftdr: 'uvm_reg_frontdoor', map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `ftdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg.set_offset`

No description available.

Signature: `set_offset(self, map: 'uvm_reg_map', offset: 'uvm_reg_addr_t', unmapped: 'bool' = False) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_reg.set_reset`

No description available.

Signature: `set_reset(self, value: 'uvm_reg_data_t', kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg.unregister`

No description available.

Signature: `unregister(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg.update`

No description available.

Signature: `update(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg.write`

No description available.

Signature: `write(self, value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_adapter`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_adapter(self, name: str = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_reg_adapter` instance

### Methods

#### `uvm_reg_adapter.bus2reg`

No description available.

Signature: `bus2reg(self, bus_item: pyuvm.uvm_sequence_item, rw: pyuvm.uvm_reg_bus_op) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bus_item` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_item` | `required` | Parameter. |
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_bus_op` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_adapter.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_adapter.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_adapter.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_adapter.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_adapter.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_adapter.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_adapter.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_item`

No description available.

Signature: `get_item(self) -> pyuvm.uvm_reg_item`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_item`

#### `uvm_reg_adapter.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.reg2bus`

No description available.

Signature: `reg2bus(self, rw: pyuvm.uvm_reg_bus_op) -> pyuvm.uvm_sequence_item`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_bus_op` | `required` | Parameter. |

Output: `uvm_sequence_item`

#### `uvm_reg_adapter.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.set_item`

No description available.

Signature: `set_item(self, item: pyuvm.uvm_reg_item) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_adapter.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_adapter.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_adapter.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_adapter.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_adapter.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_addr_logic_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_addr_logic_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_addr_logic_t` instance

### Methods

#### `uvm_reg_addr_logic_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_logic_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_logic_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_logic_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_addr_logic_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_addr_logic_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_addr_logic_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_addr_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_addr_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_addr_t` instance

### Methods

#### `uvm_reg_addr_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_addr_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_addr_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_addr_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_addr_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_backdoor`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_backdoor(self, name: 'str' = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_reg_backdoor` instance

### Methods

#### `uvm_reg_backdoor.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_backdoor.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_backdoor.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_backdoor.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_backdoor.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_backdoor.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_backdoor.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.do_post_read`

No description available.

Signature: `do_post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.do_post_write`

No description available.

Signature: `do_post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.do_pre_read`

No description available.

Signature: `do_pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.do_pre_write`

No description available.

Signature: `do_pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.is_auto_updated`

No description available.

Signature: `is_auto_updated(self, field: 'uvm_reg_field') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `field` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_field` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_backdoor.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.pre_read`

No description available.

Signature: `pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.pre_write`

No description available.

Signature: `pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.read`

No description available.

Signature: `read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.read_func`

No description available.

Signature: `read_func(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_backdoor.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_backdoor.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_backdoor.wait_for_change`

No description available.

Signature: `wait_for_change(element: 'uvm_object') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `element` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_backdoor.write`

No description available.

Signature: `write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

## Class `uvm_reg_bd_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_bd_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_reg_bd_cb` instance

### Methods

#### `uvm_reg_bd_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_reg_bd_cb.add_by_name`

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

#### `uvm_reg_bd_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_bd_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_bd_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_bd_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_bd_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_bd_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_bd_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_bd_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_bd_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_reg_bd_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_bd_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_bd_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_bd_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_bd_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_bd_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_bd_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_reg_bd_cb_iter` instance

### Methods

#### `uvm_reg_bd_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_bd_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_reg_block`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_block(self, name: 'str' = '', has_coverage: 'int' = <uvm_coverage_model_e.UVM_NO_COVERAGE: 0>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |
| `has_coverage` | `POSITIONAL_OR_KEYWORD` | `int` | `<uvm_coverage_model_e.UVM_NO_COVERAGE: 0>` | Parameter. |

Output: `uvm_reg_block` instance

### Methods

#### `uvm_reg_block.add_block`

No description available.

Signature: `add_block(self, blk: 'uvm_reg_block') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `blk` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.add_coverage`

No description available.

Signature: `add_coverage(self, models: 'uvm_reg_cvr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, path: 'str', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_block.build_coverage`

No description available.

Signature: `build_coverage(self, models: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_block.check_data_width`

No description available.

Signature: `check_data_width(width: 'int') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `width` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_block.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_block.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_block.configure`

No description available.

Signature: `configure(self, parent: 'uvm_reg_block' = None, hdl_path: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `None` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_block.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_block.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_block.create_map`

No description available.

Signature: `create_map(self, name: 'str', base_addr: 'uvm_reg_addr_t', n_bytes: 'int', endian: 'uvm_endianness_e', byte_addressing: 'bool' = True) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `base_addr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `endian` | `POSITIONAL_OR_KEYWORD` | `uvm_endianness_e` | `required` | Parameter. |
| `byte_addressing` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_map`

#### `uvm_reg_block.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_block.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_block.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_block.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.find_blocks`

No description available.

Signature: `find_blocks(name: 'str', root: 'uvm_reg_block' = None, accessor: 'uvm_object' = None) -> 'list[uvm_reg_block]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `None` | Parameter. |
| `accessor` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |

Output: `list[uvm_reg_block]`

#### `uvm_reg_block.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_backdoor`

No description available.

Signature: `get_backdoor(self, inherited: 'bool' = True) -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `inherited` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_backdoor`

#### `uvm_reg_block.get_block_by_full_name`

No description available.

Signature: `get_block_by_full_name(name: 'str') -> 'uvm_reg_block | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_block | None`

#### `uvm_reg_block.get_block_by_name`

No description available.

Signature: `get_block_by_name(self, name: 'str') -> 'uvm_reg_block | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_block | None`

#### `uvm_reg_block.get_blocks`

No description available.

Signature: `get_blocks(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg_block]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg_block]`

#### `uvm_reg_block.get_coverage`

No description available.

Signature: `get_coverage(self, is_on: 'uvm_reg_cvr_t' = <uvm_coverage_model_e.UVM_CVR_ALL: -1>) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `<uvm_coverage_model_e.UVM_CVR_ALL: -1>` | Parameter. |

Output: `bool`

#### `uvm_reg_block.get_default_door`

No description available.

Signature: `get_default_door(self) -> 'uvm_door_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_door_e`

#### `uvm_reg_block.get_default_hdl_path`

No description available.

Signature: `get_default_hdl_path(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_block.get_default_map`

No description available.

Signature: `get_default_map(self) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map`

#### `uvm_reg_block.get_default_path`

No description available.

Signature: `get_default_path(self) -> 'uvm_path_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_path_e`

#### `uvm_reg_block.get_field_by_name`

No description available.

Signature: `get_field_by_name(self, name: 'str') -> 'uvm_reg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_field`

#### `uvm_reg_block.get_fields`

No description available.

Signature: `get_fields(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg_field]`

#### `uvm_reg_block.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[str]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_reg_block.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_block.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[str]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_block.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_map_by_name`

No description available.

Signature: `get_map_by_name(self, name: 'str') -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_map`

#### `uvm_reg_block.get_maps`

No description available.

Signature: `get_maps(self) -> 'list[uvm_reg_map]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_map]`

#### `uvm_reg_block.get_mem_by_name`

No description available.

Signature: `get_mem_by_name(self, name: 'str') -> 'uvm_mem | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_mem | None`

#### `uvm_reg_block.get_memories`

No description available.

Signature: `get_memories(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_mem]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_mem]`

#### `uvm_reg_block.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_block.get_reg_by_name`

No description available.

Signature: `get_reg_by_name(self, name: 'str') -> 'uvm_reg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg | None`

#### `uvm_reg_block.get_registers`

No description available.

Signature: `get_registers(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg]`

#### `uvm_reg_block.get_root_blocks`

No description available.

Signature: `get_root_blocks() -> 'list[uvm_reg_block]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_block]`

#### `uvm_reg_block.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.get_vfield_by_name`

No description available.

Signature: `get_vfield_by_name(self, name: 'str') -> 'uvm_vreg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg_field`

#### `uvm_reg_block.get_virtual_fields`

No description available.

Signature: `get_virtual_fields(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_vreg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_vreg_field]`

#### `uvm_reg_block.get_virtual_registers`

No description available.

Signature: `get_virtual_registers(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_vreg]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_vreg]`

#### `uvm_reg_block.get_vreg_by_name`

No description available.

Signature: `get_vreg_by_name(self, name: 'str') -> 'uvm_vreg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg | None`

#### `uvm_reg_block.has_coverage`

No description available.

Signature: `has_coverage(self, models: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_block.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg_block.is_hdl_path_root`

No description available.

Signature: `is_hdl_path_root(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg_block.is_locked`

No description available.

Signature: `is_locked(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_block.lock_model`

No description available.

Signature: `lock_model(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_block.mirror`

No description available.

Signature: `mirror(self, check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_block.needs_update`

No description available.

Signature: `needs_update(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_block.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.read_mem_by_name`

No description available.

Signature: `read_mem_by_name(self, name: 'str', offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_block.read_reg_by_name`

No description available.

Signature: `read_reg_by_name(self, name: 'str', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_block.readmemh`

No description available.

Signature: `readmemh(filename: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `filename` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_block.sample`

No description available.

Signature: `sample(self, offset: 'uvm_reg_addr_t', is_read: 'bool', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `is_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.sample_values`

No description available.

Signature: `sample_values(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_block.set_backdoor`

No description available.

Signature: `set_backdoor(self, bkdr: 'uvm_reg_backdoor', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bkdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_backdoor` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_coverage`

No description available.

Signature: `set_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_block.set_default_door`

No description available.

Signature: `set_default_door(self, door: 'uvm_door_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `door` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_default_hdl_path`

No description available.

Signature: `set_default_hdl_path(self, kind: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_default_map`

No description available.

Signature: `set_default_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_hdl_path_root`

No description available.

Signature: `set_hdl_path_root(self, path: 'str', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_block.set_lock`

No description available.

Signature: `set_lock(self, v: 'bool' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `v` | `POSITIONAL_OR_KEYWORD` | `bool` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_block.set_parent`

No description available.

Signature: `set_parent(self, parent: 'uvm_reg_block') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_block.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.unlock_model`

No description available.

Signature: `unlock_model(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_block.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_block.update`

No description available.

Signature: `update(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_block.wait_for_lock`

No description available.

Signature: `wait_for_lock(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_block.write_mem_by_name`

No description available.

Signature: `write_mem_by_name(self, name: 'str', offset: 'uvm_reg_addr_t', data: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_block.write_reg_by_name`

No description available.

Signature: `write_reg_by_name(self, name: 'str', data: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_block.writememh`

No description available.

Signature: `writememh(filename: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `filename` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

## Class `uvm_reg_bus_op`

Module: `pyuvm`

uvm_reg_bus_op(kind: 'uvm_access_e' = <uvm_access_e.UVM_READ: 0>, addr: 'uvm_reg_addr_t' = 0, data: 'uvm_reg_data_t' = 0, n_bits: 'int' = 0, byte_en: 'uvm_reg_byte_en_t' = 0, status: 'uvm_status_e' = <uvm_status_e.UVM_NOT_OK: 1>)

### Constructor

Signature: `uvm_reg_bus_op(self, kind: 'uvm_access_e' = <uvm_access_e.UVM_READ: 0>, addr: 'uvm_reg_addr_t' = 0, data: 'uvm_reg_data_t' = 0, n_bits: 'int' = 0, byte_en: 'uvm_reg_byte_en_t' = 0, status: 'uvm_status_e' = <uvm_status_e.UVM_NOT_OK: 1>) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_access_e` | `<uvm_access_e.UVM_READ: 0>` | Parameter. |
| `addr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `0` | Parameter. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `byte_en` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `0` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `<uvm_status_e.UVM_NOT_OK: 1>` | Parameter. |

Output: `uvm_reg_bus_op` instance

## Class `uvm_reg_byte_en_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_byte_en_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_byte_en_t` instance

### Methods

#### `uvm_reg_byte_en_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_byte_en_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_byte_en_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_byte_en_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_byte_en_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_byte_en_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_byte_en_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_reg_cb` instance

### Methods

#### `uvm_reg_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_reg_cb.add_by_name`

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

#### `uvm_reg_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_reg_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_reg_cb_iter` instance

### Methods

#### `uvm_reg_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_reg_cbs`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_cbs(self, name: str = 'uvm_reg_cbs')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_cbs'` | Name of the object. Default is empty string. |

Output: `uvm_reg_cbs` instance

### Methods

#### `uvm_reg_cbs.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_cbs.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_cbs.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_cbs.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_cbs.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_cbs.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_cbs.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_cbs.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_cbs.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_cbs.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_cbs.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_cbs.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cbs.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_cvr_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_cvr_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_cvr_t` instance

### Methods

#### `uvm_reg_cvr_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cvr_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cvr_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_cvr_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_cvr_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_cvr_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_cvr_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_data_logic_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_data_logic_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_data_logic_t` instance

### Methods

#### `uvm_reg_data_logic_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_logic_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_logic_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_logic_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_data_logic_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_data_logic_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_data_logic_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_data_t`

Module: `pyuvm`

int([x]) -> integer

### Constructor

Signature: `uvm_reg_data_t(self, /, *args, **kwargs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `args` | `VAR_POSITIONAL` | `tuple[object, ...]` | `required` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_reg_data_t` instance

### Methods

#### `uvm_reg_data_t.as_integer_ratio`

Return a pair of integers, whose ratio is equal to the original int.

Signature: `as_integer_ratio(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_t.bit_count`

Number of ones in the binary representation of the absolute value of self.

Signature: `bit_count(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_t.bit_length`

Number of bits necessary to represent self in binary.

Signature: `bit_length(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_data_t.conjugate`

Returns self, the complex conjugate of any int.

Signature: not available

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| n/a | n/a | Any | n/a | Signature not available. |

Output: `object`

#### `uvm_reg_data_t.from_bytes`

Return the integer represented by the given array of bytes.

Signature: `from_bytes(bytes, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bytes` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

#### `uvm_reg_data_t.is_integer`

Returns True. Exists for duck type compatibility with float.is_integer.

Signature: `is_integer(self, /)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_data_t.to_bytes`

Return an array of bytes representing an integer.

Signature: `to_bytes(self, /, length=1, byteorder='big', *, signed=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `length` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | Parameter. |
| `byteorder` | `POSITIONAL_OR_KEYWORD` | `str` | `'big'` | Parameter. |
| `signed` | `KEYWORD_ONLY` | `bool` | `False` | Parameter. |

Output: `object`

## Class `uvm_reg_field`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_field(self, name: 'str' = 'uvm_reg_field') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_field'` | Name of the object. Default is empty string. |

Output: `uvm_reg_field` instance

### Methods

#### `uvm_reg_field.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_field.configure`

No description available.

Signature: `configure(self, parent: 'uvm_reg', size: 'int', lsb_pos: 'int', access: 'str', volatile: 'bool', reset: 'uvm_reg_data_t', has_reset: 'bool' = None, is_rand: 'bool' = None, individually_accessible: 'bool' = None, **kwargs) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `lsb_pos` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `access` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `volatile` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `reset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `has_reset` | `POSITIONAL_OR_KEYWORD` | `bool` | `None` | Parameter. |
| `is_rand` | `POSITIONAL_OR_KEYWORD` | `bool` | `None` | Parameter. |
| `individually_accessible` | `POSITIONAL_OR_KEYWORD` | `bool` | `None` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_field.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_field.define_access`

No description available.

Signature: `define_access(name: 'str') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_field.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_field.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_field.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_field.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.do_predict`

No description available.

Signature: `do_predict(self, rw: 'uvm_reg_item', kind: 'uvm_predict_e' = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, be: 'uvm_reg_byte_en_t' = -1) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |

Output: `None`

#### `uvm_reg_field.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.field_lock`

No description available.

Signature: `field_lock(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_field.get`

No description available.

Signature: `get(self, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_field.get_access`

No description available.

Signature: `get_access(self, map: 'uvm_reg_map' = None) -> 'str | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str | None`

#### `uvm_reg_field.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_compare`

No description available.

Signature: `get_compare(self) -> 'uvm_check_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_check_e`

#### `uvm_reg_field.get_field_by_full_name`

No description available.

Signature: `get_field_by_full_name(name: 'str') -> 'uvm_reg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_field`

#### `uvm_reg_field.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_field.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_lsb_pos`

No description available.

Signature: `get_lsb_pos(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_field.get_max_size`

No description available.

Signature: `get_max_size() -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_field.get_mirrored_value`

No description available.

Signature: `get_mirrored_value(self, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_field.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_field.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg`

#### `uvm_reg_field.get_register`

No description available.

Signature: `get_register(self) -> 'uvm_reg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg`

#### `uvm_reg_field.get_reset`

No description available.

Signature: `get_reset(self, kind: 'str' = 'HARD') -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_field.get_response`

No description available.

Signature: `get_response(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.get_value`

No description available.

Signature: `get_value(self) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_data_t`

#### `uvm_reg_field.has_reset`

No description available.

Signature: `has_reset(self, kind: 'str' = 'HARD', delete: 'bool' = False) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |
| `delete` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `bool`

#### `uvm_reg_field.is_indv_accessible`

No description available.

Signature: `is_indv_accessible(self, path: 'uvm_door_e', local_map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `local_map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_field.is_known_access`

No description available.

Signature: `is_known_access(self, map: 'uvm_reg_map' = None) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `bool`

#### `uvm_reg_field.is_volatile`

No description available.

Signature: `is_volatile(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_field.mirror`

No description available.

Signature: `mirror(self, check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_field.needs_update`

No description available.

Signature: `needs_update(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_field.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.peek`

No description available.

Signature: `peek(self, kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_field.poke`

No description available.

Signature: `poke(self, value: 'uvm_reg_data_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_field.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.post_randomize`

No description available.

Signature: `post_randomize(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_field.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.pre_randomize`

No description available.

Signature: `pre_randomize(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_field.pre_read`

No description available.

Signature: `pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.pre_write`

No description available.

Signature: `pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.predict`

No description available.

Signature: `predict(self, value: 'uvm_reg_data_t', be: 'uvm_reg_byte_en_t' = -1, kind: 'uvm_predict_e' = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_FRONTDOOR: 0>, map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_FRONTDOOR: 0>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `bool`

#### `uvm_reg_field.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.read`

No description available.

Signature: `read(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_field.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_field.set`

No description available.

Signature: `set(self, value: 'uvm_reg_data_t', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_access`

No description available.

Signature: `set_access(self, mode: 'str') -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mode` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `str`

#### `uvm_reg_field.set_compare`

No description available.

Signature: `set_compare(self, check: 'uvm_check_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_debug`

No description available.

Signature: `set_debug(self, error_on_read=None, error_on_write=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `error_on_read` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |
| `error_on_write` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_field.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_field.set_rand_mode`

No description available.

Signature: `set_rand_mode(self, rand_mode: 'bool') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rand_mode` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_reset`

No description available.

Signature: `set_reset(self, value: 'uvm_reg_data_t', kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_response`

No description available.

Signature: `set_response(self, f_response)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `f_response` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_throw_error_on_read`

No description available.

Signature: `set_throw_error_on_read(self, teor=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `teor` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_throw_error_on_write`

No description available.

Signature: `set_throw_error_on_write(self, teow=False)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `teow` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.set_volatility`

No description available.

Signature: `set_volatility(self, volatile: 'bool') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `volatile` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field.write`

No description available.

Signature: `write(self, value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_field_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_field_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_reg_field_cb` instance

### Methods

#### `uvm_reg_field_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_reg_field_cb.add_by_name`

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

#### `uvm_reg_field_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_field_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_field_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_field_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_field_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_field_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_field_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_field_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_reg_field_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_field_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_field_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_field_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_field_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_field_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_field_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_reg_field_cb_iter` instance

### Methods

#### `uvm_reg_field_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_reg_field_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_reg_fifo`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_fifo(self, name: str = 'uvm_reg_fifo', size: int = 0, n_bits: int = 0, has_coverage: int = 0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_fifo'` | Name of the object. Default is empty string. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `has_coverage` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_fifo` instance

### Methods

#### `uvm_reg_fifo.add_coverage`

No description available.

Signature: `add_coverage(self, models: 'uvm_reg_cvr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, slices: 'list[uvm_hdl_path_slice]', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `slices` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_slice]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.add_hdl_path_slice`

No description available.

Signature: `add_hdl_path_slice(self, name: 'str', offset: 'int', size: 'int', first: 'bool' = False, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `first` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.add_map`

No description available.

Signature: `add_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.backdoor_read`

No description available.

Signature: `backdoor_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.backdoor_read_func`

No description available.

Signature: `backdoor_read_func(self, rw: 'uvm_reg_item') -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_fifo.backdoor_watch`

No description available.

Signature: `backdoor_watch(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.backdoor_write`

No description available.

Signature: `backdoor_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.build`

No description available.

Signature: `build(self) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.build_coverage`

No description available.

Signature: `build_coverage(self, models: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_fifo.capacity`

No description available.

Signature: `capacity(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.check_err_list`

No description available.

Signature: `check_err_list(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_fifo.configure`

No description available.

Signature: `configure(self, blk_parent: 'uvm_reg_block', regfile_parent: 'uvm_reg_file' = None, hdl_path: 'str' = '', throw_error_on_read: 'bool' = False, throw_error_on_write: 'bool' = False, **kwargs) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `blk_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `regfile_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_file` | `None` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `throw_error_on_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `throw_error_on_write` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_fifo.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_fifo.do_check`

No description available.

Signature: `do_check(self, expected: 'uvm_reg_data_t', actual: 'uvm_reg_data_t', map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `expected` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `actual` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_fifo.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_fifo.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_fifo.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.do_predict`

No description available.

Signature: `do_predict(self, rw: pyuvm.uvm_reg_item, kind: pyuvm.uvm_predict_e = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, be: pyuvm.uvm_reg_byte_en_t = -1) -> bool`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.get`

No description available.

Signature: `get(self, fname: str = '', lineno: int = 0) -> pyuvm.uvm_reg_data_t`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_fifo.get_access_policy`

No description available.

Signature: `get_access_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_address`

No description available.

Signature: `get_address(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_fifo.get_addresses`

No description available.

Signature: `get_addresses(self, map: 'uvm_reg_map' = None) -> 'tuple[int, list[uvm_reg_addr_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `tuple[int, list[uvm_reg_addr_t]]`

#### `uvm_reg_fifo.get_backdoor`

No description available.

Signature: `get_backdoor(self, inherited: 'bool' = True) -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `inherited` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_backdoor`

#### `uvm_reg_fifo.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_fifo.get_coverage`

No description available.

Signature: `get_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.get_default_map`

No description available.

Signature: `get_default_map(self) -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map | None`

#### `uvm_reg_fifo.get_desired`

No description available.

Signature: `get_desired(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_field_by_name`

No description available.

Signature: `get_field_by_name(self, name: 'str') -> 'uvm_reg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_field`

#### `uvm_reg_fifo.get_fields`

No description available.

Signature: `get_fields(self) -> 'list[uvm_reg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_field]`

#### `uvm_reg_fifo.get_frontdoor`

No description available.

Signature: `get_frontdoor(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_frontdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_frontdoor`

#### `uvm_reg_fifo.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_fifo.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.get_hdl_path_kind`

No description available.

Signature: `get_hdl_path_kind(self, kinds: 'list[str]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kinds` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_local_map`

No description available.

Signature: `get_local_map(self, map: 'uvm_reg_map') -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_map | None`

#### `uvm_reg_fifo.get_maps`

No description available.

Signature: `get_maps(self, maps: 'list[uvm_reg_map]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maps` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_map]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.get_max_size`

No description available.

Signature: `get_max_size() -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.get_mirrored_value`

No description available.

Signature: `get_mirrored_value(self, fname: 'str' = '', lineno: 'int' = 0) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `int`

#### `uvm_reg_fifo.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.get_n_maps`

No description available.

Signature: `get_n_maps(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_offset`

No description available.

Signature: `get_offset(self, map: 'uvm_reg_map') -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_fifo.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_fifo.get_reg_by_full_name`

No description available.

Signature: `get_reg_by_full_name(full_name: 'str') -> 'uvm_reg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `full_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg | None`

#### `uvm_reg_fifo.get_reg_size`

No description available.

Signature: `get_reg_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.get_regfile`

No description available.

Signature: `get_regfile(self) -> 'uvm_reg_file'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_file`

#### `uvm_reg_fifo.get_reset`

No description available.

Signature: `get_reset(self, kind: 'str' = 'HARD') -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `int`

#### `uvm_reg_fifo.get_rights`

No description available.

Signature: `get_rights(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_reg_fifo.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.has_coverage`

No description available.

Signature: `has_coverage(self, models: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.has_reset`

No description available.

Signature: `has_reset(self, kind: 'str' = 'HARD', delete: 'bool' = False) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |
| `delete` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.include_coverage`

No description available.

Signature: `include_coverage(self, scope: 'str', models: 'uvm_reg_cvr_t', accessor: 'uvm_object' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `scope` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |
| `accessor` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.is_busy`

No description available.

Signature: `is_busy(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_fifo.is_in_map`

No description available.

Signature: `is_in_map(self, map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.mirror`

No description available.

Signature: `mirror(self, check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_fifo.needs_update`

No description available.

Signature: `needs_update() -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_fifo.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.peek`

No description available.

Signature: `peek(self, kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_fifo.poke`

No description available.

Signature: `poke(self, value: 'uvm_reg_data_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_fifo.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.post_randomize`

No description available.

Signature: `post_randomize(self) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.pre_read`

No description available.

Signature: `pre_read(self, rw: pyuvm.uvm_reg_item) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.pre_write`

No description available.

Signature: `pre_write(self, rw: pyuvm.uvm_reg_item) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.predict`

No description available.

Signature: `predict(self, value: 'uvm_reg_data_t', be: 'uvm_reg_byte_en_t' = -1, kind: 'uvm_predict_e' = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_FRONTDOOR: 0>, map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_FRONTDOOR: 0>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `bool`

#### `uvm_reg_fifo.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.read`

No description available.

Signature: `read(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_fifo.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.sample`

No description available.

Signature: `sample(self, data: 'uvm_reg_data_t', byte_en: 'uvm_reg_data_t', is_read: 'bool', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `byte_en` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `is_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.sample_values`

No description available.

Signature: `sample_values(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.set`

No description available.

Signature: `set(self, value: pyuvm.uvm_reg_data_t, fname: str = '', lineno: int = 0) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_backdoor`

No description available.

Signature: `set_backdoor(self, bkdr: 'uvm_reg_backdoor', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bkdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_backdoor` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_compare`

No description available.

Signature: `set_compare(self, check: pyuvm.uvm_check_e = <uvm_check_e.UVM_CHECK: 1>) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_CHECK: 1>` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_coverage`

No description available.

Signature: `set_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_fifo.set_desired`

No description available.

Signature: `set_desired(self, value)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_frontdoor`

No description available.

Signature: `set_frontdoor(self, ftdr: 'uvm_reg_frontdoor', map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `ftdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_fifo.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_fifo.set_offset`

No description available.

Signature: `set_offset(self, map: 'uvm_reg_map', offset: 'uvm_reg_addr_t', unmapped: 'bool' = False) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_reset`

No description available.

Signature: `set_reset(self, value: 'uvm_reg_data_t', kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.size`

No description available.

Signature: `size(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_fifo.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_fifo.unregister`

No description available.

Signature: `unregister(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_fifo.update`

No description available.

Signature: `update(self, path: pyuvm.uvm_door_e = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: pyuvm.uvm_reg_map = None, parent: pyuvm.uvm_sequence_base = None, prior: int = -1, extension: pyuvm.uvm_object = None, fname: str = '', lineno: int = 0) -> pyuvm.uvm_status_e`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_fifo.write`

No description available.

Signature: `write(self, value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_file`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_file(self, name: 'str' = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Name of the object. Default is empty string. |

Output: `uvm_reg_file` instance

### Methods

#### `uvm_reg_file.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, path: 'str', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_file.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_file.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_file.configure`

No description available.

Signature: `configure(self, blk_parent: 'uvm_reg_block', regfile_parent: 'uvm_reg_file', hdl_path: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `blk_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `regfile_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_file` | `required` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_file.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_file.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_file.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_file.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_file.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_file.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_file.get_default_hdl_path`

No description available.

Signature: `get_default_hdl_path(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_file.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[str]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_reg_file.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_file.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[str]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_file.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_file.get_regfile`

No description available.

Signature: `get_regfile(self) -> 'uvm_reg_file'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_file`

#### `uvm_reg_file.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg_file.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.set_default_hdl_path`

No description available.

Signature: `set_default_hdl_path(self, kind: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_file.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_file.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_file.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_file.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_file.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_frontdoor`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_frontdoor(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_frontdoor` instance

## Class `uvm_reg_indirect_data`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_indirect_data(self, name: str = 'uvm_reg_indirect', n_bits: int = 0, has_coverage: int = 0) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_indirect'` | Name of the object. Default is empty string. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `has_coverage` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_indirect_data` instance

### Methods

#### `uvm_reg_indirect_data.add_coverage`

No description available.

Signature: `add_coverage(self, models: 'uvm_reg_cvr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.add_hdl_path`

No description available.

Signature: `add_hdl_path(self, slices: 'list[uvm_hdl_path_slice]', kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `slices` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_slice]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.add_hdl_path_slice`

No description available.

Signature: `add_hdl_path_slice(self, name: 'str', offset: 'int', size: 'int', first: 'bool' = False, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `first` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.add_map`

No description available.

Signature: `add_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.backdoor_read`

No description available.

Signature: `backdoor_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.backdoor_read_func`

No description available.

Signature: `backdoor_read_func(self, rw: 'uvm_reg_item') -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_data.backdoor_watch`

No description available.

Signature: `backdoor_watch(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_indirect_data.backdoor_write`

No description available.

Signature: `backdoor_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.build_coverage`

No description available.

Signature: `build_coverage(self, models: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_indirect_data.check_err_list`

No description available.

Signature: `check_err_list(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_indirect_data.clear_hdl_path`

No description available.

Signature: `clear_hdl_path(self, kind: 'str' = 'RTL') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'RTL'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_indirect_data.configure`

No description available.

Signature: `configure(self, blk_parent: 'uvm_reg_block', regfile_parent: 'uvm_reg_file' = None, hdl_path: 'str' = '', throw_error_on_read: 'bool' = False, throw_error_on_write: 'bool' = False, **kwargs) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `blk_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `regfile_parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_file` | `None` | Parameter. |
| `hdl_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `throw_error_on_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `throw_error_on_write` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_indirect_data.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_data.do_check`

No description available.

Signature: `do_check(self, expected: 'uvm_reg_data_t', actual: 'uvm_reg_data_t', map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `expected` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `actual` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_indirect_data.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_indirect_data.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_data.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.do_predict`

No description available.

Signature: `do_predict(self, rw: 'uvm_reg_item', kind: 'uvm_predict_e', be: 'uvm_reg_byte_en_t' = -1) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.get`

No description available.

Signature: `get(self, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_indirect_data.get_access_policy`

No description available.

Signature: `get_access_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_address`

No description available.

Signature: `get_address(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_indirect_data.get_addresses`

No description available.

Signature: `get_addresses(self, map: 'uvm_reg_map' = None) -> 'tuple[int, list[uvm_reg_addr_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `tuple[int, list[uvm_reg_addr_t]]`

#### `uvm_reg_indirect_data.get_backdoor`

No description available.

Signature: `get_backdoor(self, inherited: 'bool' = True) -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `inherited` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_backdoor`

#### `uvm_reg_indirect_data.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_indirect_data.get_coverage`

No description available.

Signature: `get_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.get_default_map`

No description available.

Signature: `get_default_map(self) -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map | None`

#### `uvm_reg_indirect_data.get_desired`

No description available.

Signature: `get_desired(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_field_by_name`

No description available.

Signature: `get_field_by_name(self, name: 'str') -> 'uvm_reg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_field`

#### `uvm_reg_indirect_data.get_fields`

No description available.

Signature: `get_fields(self) -> 'list[uvm_reg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_field]`

#### `uvm_reg_indirect_data.get_frontdoor`

No description available.

Signature: `get_frontdoor(self, map: 'uvm_reg_map' = None) -> 'uvm_reg_frontdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_frontdoor`

#### `uvm_reg_indirect_data.get_full_hdl_path`

No description available.

Signature: `get_full_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '', separator: 'str' = '.') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `separator` | `POSITIONAL_OR_KEYWORD` | `str` | `'.'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_indirect_data.get_hdl_path`

No description available.

Signature: `get_hdl_path(self, paths: 'list[uvm_hdl_path_concat]', kind: 'str' = '') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `paths` | `POSITIONAL_OR_KEYWORD` | `list[uvm_hdl_path_concat]` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.get_hdl_path_kind`

No description available.

Signature: `get_hdl_path_kind(self, kinds: 'list[str]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kinds` | `POSITIONAL_OR_KEYWORD` | `list[str]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_local_map`

No description available.

Signature: `get_local_map(self, map: 'uvm_reg_map') -> 'uvm_reg_map | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_map | None`

#### `uvm_reg_indirect_data.get_maps`

No description available.

Signature: `get_maps(self, maps: 'list[uvm_reg_map]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maps` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_map]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.get_max_size`

No description available.

Signature: `get_max_size() -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_indirect_data.get_mirrored_value`

No description available.

Signature: `get_mirrored_value(self, fname: 'str' = '', lineno: 'int' = 0) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `int`

#### `uvm_reg_indirect_data.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_indirect_data.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_indirect_data.get_n_maps`

No description available.

Signature: `get_n_maps(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_indirect_data.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_offset`

No description available.

Signature: `get_offset(self, map: 'uvm_reg_map') -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_indirect_data.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_indirect_data.get_reg_by_full_name`

No description available.

Signature: `get_reg_by_full_name(full_name: 'str') -> 'uvm_reg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `full_name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg | None`

#### `uvm_reg_indirect_data.get_reg_size`

No description available.

Signature: `get_reg_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_indirect_data.get_regfile`

No description available.

Signature: `get_regfile(self) -> 'uvm_reg_file'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_file`

#### `uvm_reg_indirect_data.get_reset`

No description available.

Signature: `get_reset(self, kind: 'str' = 'HARD') -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `int`

#### `uvm_reg_indirect_data.get_rights`

No description available.

Signature: `get_rights(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_reg_indirect_data.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.has_coverage`

No description available.

Signature: `has_coverage(self, models: 'uvm_reg_cvr_t') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.has_hdl_path`

No description available.

Signature: `has_hdl_path(self, kind: 'str' = '') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.has_reset`

No description available.

Signature: `has_reset(self, kind: 'str' = 'HARD', delete: 'bool' = False) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |
| `delete` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.include_coverage`

No description available.

Signature: `include_coverage(self, scope: 'str', models: 'uvm_reg_cvr_t', accessor: 'uvm_object' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `scope` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `models` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |
| `accessor` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.is_busy`

No description available.

Signature: `is_busy(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_indirect_data.is_in_map`

No description available.

Signature: `is_in_map(self, map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.mirror`

No description available.

Signature: `mirror(self, check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_data.needs_update`

No description available.

Signature: `needs_update() -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_indirect_data.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.peek`

No description available.

Signature: `peek(self, kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_data.poke`

No description available.

Signature: `poke(self, value: 'uvm_reg_data_t', kind: 'str' = '', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_data.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.post_read`

No description available.

Signature: `post_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.post_write`

No description available.

Signature: `post_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.pre_read`

No description available.

Signature: `pre_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.pre_write`

No description available.

Signature: `pre_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.predict`

No description available.

Signature: `predict(self, value: 'uvm_reg_data_t', be: 'uvm_reg_byte_en_t' = -1, kind: 'uvm_predict_e' = <uvm_predict_e.UVM_PREDICT_DIRECT: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_FRONTDOOR: 0>, map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `be` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_byte_en_t` | `-1` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_predict_e` | `<uvm_predict_e.UVM_PREDICT_DIRECT: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_FRONTDOOR: 0>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `bool`

#### `uvm_reg_indirect_data.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.read`

No description available.

Signature: `read(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_data.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.sample`

No description available.

Signature: `sample(self, data: 'uvm_reg_data_t', byte_en: 'uvm_reg_data_t', is_read: 'bool', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `data` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `byte_en` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `is_read` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.sample_values`

No description available.

Signature: `sample_values(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_indirect_data.set`

No description available.

Signature: `set(self, value: 'uvm_reg_data_t', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_backdoor`

No description available.

Signature: `set_backdoor(self, bkdr: 'uvm_reg_backdoor', fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bkdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_backdoor` | `required` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_coverage`

No description available.

Signature: `set_coverage(self, is_on: 'uvm_reg_cvr_t') -> 'uvm_reg_cvr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `is_on` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_cvr_t` | `required` | Parameter. |

Output: `uvm_reg_cvr_t`

#### `uvm_reg_indirect_data.set_desired`

No description available.

Signature: `set_desired(self, value)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_frontdoor`

No description available.

Signature: `set_frontdoor(self, ftdr: 'uvm_reg_frontdoor', map: 'uvm_reg_map' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `ftdr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_indirect_data.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_indirect_data.set_offset`

No description available.

Signature: `set_offset(self, map: 'uvm_reg_map', offset: 'uvm_reg_addr_t', unmapped: 'bool' = False) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_reset`

No description available.

Signature: `set_reset(self, value: 'uvm_reg_data_t', kind: 'str' = 'HARD') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'HARD'` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_data.unregister`

No description available.

Signature: `unregister(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_data.update`

No description available.

Signature: `update(self, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_data.write`

No description available.

Signature: `write(self, value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0, **kwargs) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `kwargs` | `VAR_KEYWORD` | `dict[str, object]` | `required` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_indirect_ftdr_seq`

Module: `pyuvm`

The uvm_sequence creates a series of sequence

### Constructor

Signature: `uvm_reg_indirect_ftdr_seq(self, addr_reg: pyuvm.uvm_reg, idx: int, data_reg: pyuvm.uvm_reg) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `addr_reg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `data_reg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |

Output: `uvm_reg_indirect_ftdr_seq` instance

### Methods

#### `uvm_reg_indirect_ftdr_seq.atomic_lock`

No description available.

Signature: `atomic_lock(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.atomic_unlock`

No description available.

Signature: `atomic_unlock(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.body`

This function gets launched in a thread when you run start()

Signature: `body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.do_reg_item`

No description available.

Signature: `do_reg_item(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_ftdr_seq.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.finish_item`

No description available.

Signature: `finish_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_response`

No description available.

Signature: `get_response(self, transaction_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `transaction_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.mirror_reg`

No description available.

Signature: `mirror_reg(self, rg: 'uvm_reg', check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_ftdr_seq.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.peek_mem`

No description available.

Signature: `peek_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_ftdr_seq.peek_reg`

No description available.

Signature: `peek_reg(self, rg: 'uvm_reg', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_ftdr_seq.poke_mem`

No description available.

Signature: `poke_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_ftdr_seq.poke_reg`

No description available.

Signature: `poke_reg(self, rg: 'uvm_reg', value: 'uvm_reg_data_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_ftdr_seq.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.post_body`

This function gets launced AFTER the function body() is started

Signature: `post_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.pre_body`

This function gets launced BEFORE the function body() is started

Signature: `pre_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.read_mem`

No description available.

Signature: `read_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_ftdr_seq.read_reg`

No description available.

Signature: `read_reg(self, rg: 'uvm_reg', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_indirect_ftdr_seq.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_indirect_ftdr_seq.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_indirect_ftdr_seq.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_indirect_ftdr_seq.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.start`

Launch this sequence on the sequencer. Seqr cannot be None.

Signature: `start(self, sequencer: 'uvm_sequencer_base', parent_sequence: 'uvm_sequence_base' = None, this_priority: 'int' = -1, call_pre_post: 'bool' = True) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `sequencer` | `POSITIONAL_OR_KEYWORD` | `uvm_sequencer_base` | `required` | Parameter. |
| `parent_sequence` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `this_priority` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `call_pre_post` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | If set to true (default), then pre_body and |

Output: `None`

#### `uvm_reg_indirect_ftdr_seq.start_item`

Sends an item to the sequencer and waits to be notified

Signature: `start_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The sequence item to send to the driver. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_indirect_ftdr_seq.update_reg`

No description available.

Signature: `update_reg(self, rg: 'uvm_reg', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_ftdr_seq.write_mem`

No description available.

Signature: `write_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_indirect_ftdr_seq.write_reg`

No description available.

Signature: `write_reg(self, rg: 'uvm_reg', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_item`

Module: `pyuvm`

The pyuvm uvm_sequence_item has events to

### Constructor

Signature: `uvm_reg_item(self, name: 'str' = '')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Object name |

Output: `uvm_reg_item` instance

### Methods

#### `uvm_reg_item.accept_tr`

:param accept_time: Simulation time when the transaction is accepted

Signature: `accept_tr(self, accept_time=0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accept_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time when the transaction is accepted |

Output: `object`

#### `uvm_reg_item.begin_tr`

:param begin_time: Simulation time at which

Signature: `begin_tr(self, begin_time=0, parent_handle=None) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `begin_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which |
| `parent_handle` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `int`

#### `uvm_reg_item.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_item.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_item.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_item.disable_recording`

Not implemented

Signature: `disable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_accept_tr`

User definable method to add to ``accept_tr()``

Signature: `do_accept_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_begin_tr`

User definable method

Signature: `do_begin_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_item.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_item.do_end_tr`

Not implemented

Signature: `do_end_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_item.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.enable_recording`

Not implemented

Signature: `enable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.end_tr`

:param end_time: Simulation time at which the transaction

Signature: `end_tr(self, end_time=0, free_handle=True) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `end_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which the transaction |
| `free_handle` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_reg_item.get_accept_time`

:return: Accept time of transaction

Signature: `get_accept_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_bd_kind`

No description available.

Signature: `get_bd_kind(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_item.get_begin_time`

:return: Begin time of transaction

Signature: `get_begin_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.get_door`

No description available.

Signature: `get_door(self) -> 'uvm_door_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_door_e`

#### `uvm_reg_item.get_element`

No description available.

Signature: `get_element(self) -> 'uvm_object'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_object`

#### `uvm_reg_item.get_element_kind`

No description available.

Signature: `get_element_kind(self) -> 'uvm_elem_kind_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_elem_kind_e`

#### `uvm_reg_item.get_end_time`

:return: End time of transaction

Signature: `get_end_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.get_event_pool`

Not implemented

Signature: `get_event_pool(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_extension`

No description available.

Signature: `get_extension(self) -> 'uvm_object'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_object`

#### `uvm_reg_item.get_fname`

No description available.

Signature: `get_fname(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_item.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_initiator`

:return: initiator

Signature: `get_initiator(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_kind`

No description available.

Signature: `get_kind(self) -> 'uvm_access_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_access_e`

#### `uvm_reg_item.get_line`

No description available.

Signature: `get_line(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.get_local_map`

No description available.

Signature: `get_local_map(self) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map`

#### `uvm_reg_item.get_map`

No description available.

Signature: `get_map(self) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map`

#### `uvm_reg_item.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_offset`

No description available.

Signature: `get_offset(self) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_item.get_parent_sequence`

No description available.

Signature: `get_parent_sequence(self) -> 'uvm_sequence_base'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_sequence_base`

#### `uvm_reg_item.get_priority`

No description available.

Signature: `get_priority(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.get_status`

No description available.

Signature: `get_status(self) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_status_e`

#### `uvm_reg_item.get_tr_handle`

Not implemented

Signature: `get_tr_handle(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_transaction_id`

:return: Transaction ID

Signature: `get_transaction_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.get_value`

No description available.

Signature: `get_value(self, idx: 'int' = 0) -> 'uvm_reg_data_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_reg_data_t`

#### `uvm_reg_item.get_value_array`

No description available.

Signature: `get_value_array(self) -> 'list[uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `list[uvm_reg_data_t]`

#### `uvm_reg_item.get_value_size`

No description available.

Signature: `get_value_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_item.is_active`

Not implemented

Signature: `is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_item.is_recording_enabled`

Not implemented

Signature: `is_recording_enabled(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_item.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.set_bd_kind`

No description available.

Signature: `set_bd_kind(self, bd_kind: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bd_kind` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_context`

Use this to link a new response transaction to the request transaction.

Signature: `set_context(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The request transaction |

Output: `None`

#### `uvm_reg_item.set_door`

No description available.

Signature: `set_door(self, door: 'uvm_door_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `door` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_element`

No description available.

Signature: `set_element(self, element: 'uvm_object') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `element` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_element_kind`

No description available.

Signature: `set_element_kind(self, element_kind: 'uvm_elem_kind_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `element_kind` | `POSITIONAL_OR_KEYWORD` | `uvm_elem_kind_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_extension`

No description available.

Signature: `set_extension(self, value: 'uvm_object') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_fname`

No description available.

Signature: `set_fname(self, fname: 'str') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_id_info`

:param other: uvm_transaction with transaction_id

Signature: `set_id_info(self, other)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `other` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | uvm_transaction with transaction_id |

Output: `None`

#### `uvm_reg_item.set_initiator`

:param initiator: initiator to set

Signature: `set_initiator(self, initiator)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | initiator to set |

Output: `None`

#### `uvm_reg_item.set_kind`

No description available.

Signature: `set_kind(self, kind: 'uvm_access_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `uvm_access_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_line`

No description available.

Signature: `set_line(self, line: 'int') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `line` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_item.set_local_map`

No description available.

Signature: `set_local_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_map`

No description available.

Signature: `set_map(self, map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_item.set_offset`

No description available.

Signature: `set_offset(self, offset: 'uvm_reg_addr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_parent_sequence`

No description available.

Signature: `set_parent_sequence(self, parent: 'uvm_sequence_base') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_priority`

No description available.

Signature: `set_priority(self, value: 'int') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_status`

No description available.

Signature: `set_status(self, status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_transaction_id`

:param txn_id: Transaction ID

Signature: `set_transaction_id(self, txn_id)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Transaction ID |

Output: `None`

#### `uvm_reg_item.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_value`

No description available.

Signature: `set_value(self, value: 'uvm_reg_data_t', idx: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_value_array`

No description available.

Signature: `set_value_array(self, value: 'list[uvm_reg_data_t]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `value` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_data_t]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.set_value_size`

No description available.

Signature: `set_value_size(self, sz: 'int') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `sz` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_item.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_item.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_map`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_map(self, name: 'str' = 'uvm_reg_map')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_map'` | Name of the object. Default is empty string. |

Output: `uvm_reg_map` instance

### Methods

#### `uvm_reg_map.add_mem`

No description available.

Signature: `add_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', rights: 'str' = 'RW', unmapped: 'bool' = False, frontdoor: 'uvm_reg_frontdoor' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `rights` | `POSITIONAL_OR_KEYWORD` | `str` | `'RW'` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `frontdoor` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_map.add_reg`

No description available.

Signature: `add_reg(self, rg: 'uvm_reg', offset: 'uvm_reg_addr_t', rights: 'str' = 'RW', unmapped: 'bool' = False, frontdoor: 'uvm_reg_frontdoor' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `rights` | `POSITIONAL_OR_KEYWORD` | `str` | `'RW'` | Parameter. |
| `unmapped` | `POSITIONAL_OR_KEYWORD` | `bool` | `False` | Parameter. |
| `frontdoor` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_frontdoor` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_map.add_submap`

No description available.

Signature: `add_submap(self, child_map: 'uvm_reg_map', offset: 'uvm_reg_addr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `child_map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.backdoor`

No description available.

Signature: `backdoor() -> 'uvm_reg_backdoor'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_backdoor`

#### `uvm_reg_map.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.clone_and_update`

No description available.

Signature: `clone_and_update(self, rights: 'str') -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rights` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_reg_map`

#### `uvm_reg_map.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_map.configure`

No description available.

Signature: `configure(self, parent: 'uvm_reg_block', base_addr: 'uvm_reg_addr_t', n_bytes: 'int' = None, endian: 'uvm_endianness_e' = None, byte_addressing: 'bool' = True) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `base_addr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | Parameter. |
| `endian` | `POSITIONAL_OR_KEYWORD` | `uvm_endianness_e` | `None` | Parameter. |
| `byte_addressing` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_reg_map.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_map.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_map.do_bus_read`

No description available.

Signature: `do_bus_read(self, rw: 'uvm_reg_item', sequencer: 'uvm_sequencer_base', adapter: 'uvm_reg_adapter') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `sequencer` | `POSITIONAL_OR_KEYWORD` | `uvm_sequencer_base` | `required` | Parameter. |
| `adapter` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_adapter` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.do_bus_write`

No description available.

Signature: `do_bus_write(self, rw: 'uvm_reg_item', sequencer: 'uvm_sequencer_base', adapter: 'uvm_reg_adapter') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `sequencer` | `POSITIONAL_OR_KEYWORD` | `uvm_sequencer_base` | `required` | Parameter. |
| `adapter` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_adapter` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_map.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_map.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_map.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.do_read`

No description available.

Signature: `do_read(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.do_write`

No description available.

Signature: `do_write(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_adapter`

No description available.

Signature: `get_adapter(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'uvm_reg_adapter'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `uvm_reg_adapter`

#### `uvm_reg_map.get_addr_unit_bytes`

No description available.

Signature: `get_addr_unit_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_map.get_auto_predict`

No description available.

Signature: `get_auto_predict(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_map.get_base_addr`

No description available.

Signature: `get_base_addr(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_map.get_check_on_read`

No description available.

Signature: `get_check_on_read(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_map.get_endian`

No description available.

Signature: `get_endian(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'uvm_endianness_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `uvm_endianness_e`

#### `uvm_reg_map.get_fields`

No description available.

Signature: `get_fields(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg_field]`

#### `uvm_reg_map.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_reg_map.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_mem_by_offset`

No description available.

Signature: `get_mem_by_offset(self, offset: 'uvm_reg_addr_t') -> 'uvm_mem'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |

Output: `uvm_mem`

#### `uvm_reg_map.get_mem_map_info`

No description available.

Signature: `get_mem_map_info(self, mem: 'uvm_mem', error: 'bool') -> 'uvm_reg_map_info'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `error` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `uvm_reg_map_info`

#### `uvm_reg_map.get_memories`

No description available.

Signature: `get_memories(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_mem]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_mem]`

#### `uvm_reg_map.get_n_bytes`

No description available.

Signature: `get_n_bytes(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `int`

#### `uvm_reg_map.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_offset`

No description available.

Signature: `get_offset(self) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_map.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_reg_map.get_parent_map`

No description available.

Signature: `get_parent_map(self) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map`

#### `uvm_reg_map.get_physical_addresses`

No description available.

Signature: `get_physical_addresses(self, base_addr: 'uvm_reg_addr_t', mem_offset: 'uvm_reg_addr_t', n_bytes: 'int') -> 'tuple[int, list[uvm_reg_addr_t]]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `base_addr` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `mem_offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `n_bytes` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `tuple[int, list[uvm_reg_addr_t]]`

#### `uvm_reg_map.get_reg_by_offset`

No description available.

Signature: `get_reg_by_offset(self, offset: 'uvm_reg_addr_t', read: 'bool' = True) -> 'uvm_reg | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `read` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg | None`

#### `uvm_reg_map.get_reg_map_info`

No description available.

Signature: `get_reg_map_info(self, rg: 'uvm_reg', error: 'bool' = True) -> 'uvm_reg_map_info | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `error` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `uvm_reg_map_info | None`

#### `uvm_reg_map.get_registers`

No description available.

Signature: `get_registers(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg]`

#### `uvm_reg_map.get_root_map`

No description available.

Signature: `get_root_map(self) -> 'uvm_reg_map'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map`

#### `uvm_reg_map.get_sequencer`

No description available.

Signature: `get_sequencer(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'uvm_sequencer_base'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `uvm_sequencer_base`

#### `uvm_reg_map.get_size`

No description available.

Signature: `get_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_map.get_submap_offset`

No description available.

Signature: `get_submap_offset(self, submap: 'uvm_reg_map') -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `submap` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_reg_map.get_submaps`

No description available.

Signature: `get_submaps(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_reg_map]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_reg_map]`

#### `uvm_reg_map.get_transaction_order_policy`

No description available.

Signature: `get_transaction_order_policy(self) -> 'uvm_reg_transaction_order_policy'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_transaction_order_policy`

#### `uvm_reg_map.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.get_virtual_fields`

No description available.

Signature: `get_virtual_fields(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_vreg_field]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_vreg_field]`

#### `uvm_reg_map.get_virtual_registers`

No description available.

Signature: `get_virtual_registers(self, hier: 'uvm_hier_e' = <uvm_hier_e.UVM_HIER: 1>) -> 'list[uvm_vreg]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `hier` | `POSITIONAL_OR_KEYWORD` | `uvm_hier_e` | `<uvm_hier_e.UVM_HIER: 1>` | Parameter. |

Output: `list[uvm_vreg]`

#### `uvm_reg_map.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.perform_accesses`

No description available.

Signature: `perform_accesses(self, accesses: 'list[uvm_reg_bus_op]', rw: 'uvm_reg_item', adapter: 'uvm_reg_adapter', sequencer: 'uvm_sequencer_base') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accesses` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_bus_op]` | `required` | Parameter. |
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |
| `adapter` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_adapter` | `required` | Parameter. |
| `sequencer` | `POSITIONAL_OR_KEYWORD` | `uvm_sequencer_base` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.reset`

No description available.

Signature: `reset(self, kind: 'str' = 'SOFT') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `'SOFT'` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_adapter`

No description available.

Signature: `set_adapter(self, adapter) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `adapter` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_auto_predict`

No description available.

Signature: `set_auto_predict(self, on: 'bool' = True) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_base_addr`

No description available.

Signature: `set_base_addr(self, offset: 'uvm_reg_addr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_check_on_read`

No description available.

Signature: `set_check_on_read(self, on: 'bool' = True) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_map.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_map.set_sequencer`

No description available.

Signature: `set_sequencer(self, sequencer: 'uvm_sequencer', adapter: 'uvm_reg_adapter' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `sequencer` | `POSITIONAL_OR_KEYWORD` | `uvm_sequencer` | `required` | Parameter. |
| `adapter` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_adapter` | `None` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_submap_offset`

No description available.

Signature: `set_submap_offset(self, submap: 'uvm_reg_map', offset: 'uvm_reg_addr_t') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `submap` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_transaction_order_policy`

No description available.

Signature: `set_transaction_order_policy(self, pol: 'uvm_reg_transaction_order_policy') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `pol` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_transaction_order_policy` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_map.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_map.unregister`

No description available.

Signature: `unregister(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

## Class `uvm_reg_map_addr_range`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_map_addr_range(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map_addr_range` instance

## Class `uvm_reg_map_info`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_reg_map_info(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_map_info` instance

## Class `uvm_reg_mem_test_e`

Module: `pyuvm`

Enum where members are also (and must be) ints

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_DO_REG_HW_RESET` | `1` | Enum member. |
| `UVM_DO_REG_BIT_BASH` | `2` | Enum member. |
| `UVM_DO_REG_ACCESS` | `4` | Enum member. |
| `UVM_DO_MEM_ACCESS` | `8` | Enum member. |
| `UVM_DO_SHARED_ACCESS` | `16` | Enum member. |
| `UVM_DO_MEM_WALK` | `32` | Enum member. |
| `UVM_DO_ALL_REG_MEM_TESTS` | `18446744073709551615` | Enum member. |

## Class `uvm_reg_predictor`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_predictor(self, name: 'str', parent: 'uvm_component') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The name of the component. Used in the UVM hierarchy |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | The parent component.  If None, the parent is uvm_root |

Output: `uvm_reg_predictor` instance

### Methods

#### `uvm_reg_predictor.add_child`

No description available.

Signature: `add_child(self, name, child)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `child` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_predictor.add_logging_handler`

:param handler: The logging handler

Signature: `add_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler |

Output: `object`

#### `uvm_reg_predictor.add_logging_handler_hier`

Add an additional handler all the way down the component hierarchy

Signature: `add_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | A logging.Handler object |

Output: `object`

#### `uvm_reg_predictor.build_phase`

No description available.

Signature: `build_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.cdb_get`

A convenience routine that retrieves an object from

Signature: `cdb_get(self, label, inst_path='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label used to store the value |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | The path below this component |

Output: `object`

#### `uvm_reg_predictor.cdb_set`

A convenience routing to store an object in the config_db using

Signature: `cdb_set(self, label, value, inst_path='*')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `label` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The label to use to retrieve it |
| `value` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to store |
| `inst_path` | `POSITIONAL_OR_KEYWORD` | `str` | `'*'` | A path with globs or if left blank |

Output: `object`

#### `uvm_reg_predictor.check_phase`

No description available.

Signature: `check_phase(self, phase: 'uvm_phase')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `phase` | `POSITIONAL_OR_KEYWORD` | `uvm_phase` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_predictor.clear_children`

Removes the direct children from this component.

Signature: `clear_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.clear_components`

No description available.

Signature: `clear_components()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.clear_hierarchy`

Removes self from the UVM hierarchy

Signature: `clear_hierarchy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_predictor.connect_phase`

No description available.

Signature: `connect_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_predictor.create`

:return: new object from factory

Signature: `create(name='', parent=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_predictor.disable_logging`

:returns: None

Signature: `disable_logging(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.disable_logging_hier`

Disable logging for this component and all the way down the hierarchy

Signature: `disable_logging_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_predictor.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_predictor.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_predictor.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.drop_objection`

Drop an objection, usually at the end of the ``run_phase()``

Signature: `drop_objection(self, description='')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Not used, but kept for symmetry with raise_objection |

Output: `None`

#### `uvm_reg_predictor.end_of_elaboration_phase`

No description available.

Signature: `end_of_elaboration_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.extract_phase`

No description available.

Signature: `extract_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.final_phase`

No description available.

Signature: `final_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.flush`

No description available.

Signature: `flush(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_predictor.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_child`

13.1.3.4

Signature: `get_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | child's name |

Output: `object`

#### `uvm_reg_predictor.get_children`

13.1.3.3

Signature: `get_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_default_logging_level`

:returns: The default logging level

Signature: `get_default_logging_level()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_depth`

13.1.3.8

Signature: `get_depth(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_full_name`

:return: This component's name concatenated to parent name.

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_initial_logger_name`

:returns: The name of the initial logger

Signature: `get_initial_logger_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_num_children`

13.1.3.5

Signature: `get_num_children(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_parent`

:return: parent object

Signature: `get_parent(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.has_child`

13.1.3.6

Signature: `has_child(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of child the object |

Output: `bool`

#### `uvm_reg_predictor.lookup`

13.1.3.7

Signature: `lookup(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | The search name |

Output: `object`

#### `uvm_reg_predictor.objection`

No description available.

Signature: `objection(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.pre_predict`

No description available.

Signature: `pre_predict(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_predictor.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.raise_objection`

Raise an objection, usually at the start of the ``run_phase()``

Signature: `raise_objection(self, description='', stacklevel=1)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `description` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | A meaningful description speeds up timeout debug |
| `stacklevel` | `POSITIONAL_OR_KEYWORD` | `int` | `1` | For debug, increase to associate with higher level caller |

Output: `None`

#### `uvm_reg_predictor.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.remove_logging_handler`

:param handler: The logging handler to remove

Signature: `remove_logging_handler(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | The logging handler to remove |

Output: `object`

#### `uvm_reg_predictor.remove_logging_handler_hier`

Remove a handler from all loggers below this component

Signature: `remove_logging_handler_hier(self, handler)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `handler` | `POSITIONAL_OR_KEYWORD` | `logging.Handler` | `required` | logging handler |

Output: `object`

#### `uvm_reg_predictor.remove_streaming_handler`

:returns: None

Signature: `remove_streaming_handler(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.remove_streaming_handler_hier`

Remove this component's streaming handler and all the way down

Signature: `remove_streaming_handler_hier(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.report_phase`

No description available.

Signature: `report_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.run_phase`

No description available.

Signature: `run_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.set_default_logging_level`

:param default_logging_level: The default logging level

Signature: `set_default_logging_level(default_logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `default_logging_level` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The default logging level |

Output: `None`

#### `uvm_reg_predictor.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_predictor.set_logging_level`

:param logging_level: The logging level

Signature: `set_logging_level(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | The logging level |

Output: `None`

#### `uvm_reg_predictor.set_logging_level_hier`

Set the logging level for this component's logger

Signature: `set_logging_level_hier(self, logging_level)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `logging_level` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | typically a constant from logging module |

Output: `None`

#### `uvm_reg_predictor.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_predictor.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_predictor.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.start_of_simulation_phase`

No description available.

Signature: `start_of_simulation_phase(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_predictor.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_read_only_cbs`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_read_only_cbs(self, name: str = 'uvm_reg_read_only_cbs')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_read_only_cbs'` | Name of the object. Default is empty string. |

Output: `uvm_reg_read_only_cbs` instance

### Methods

#### `uvm_reg_read_only_cbs.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_read_only_cbs.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_read_only_cbs.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_read_only_cbs.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_read_only_cbs.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_read_only_cbs.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_read_only_cbs.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_read_only_cbs.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_read_only_cbs.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_read_only_cbs.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_seq_base`

Module: `pyuvm`

The pyuvm uvm_sequence_item has events to

### Constructor

Signature: `uvm_reg_seq_base(self, name: 'str' = 'uvm_reg_seq_base')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_seq_base'` | Object name |

Output: `uvm_reg_seq_base` instance

### Methods

#### `uvm_reg_seq_base.accept_tr`

:param accept_time: Simulation time when the transaction is accepted

Signature: `accept_tr(self, accept_time=0)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `accept_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time when the transaction is accepted |

Output: `object`

#### `uvm_reg_seq_base.begin_tr`

:param begin_time: Simulation time at which

Signature: `begin_tr(self, begin_time=0, parent_handle=None) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `begin_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which |
| `parent_handle` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | Parameter. |

Output: `int`

#### `uvm_reg_seq_base.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_seq_base.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_seq_base.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_seq_base.disable_recording`

Not implemented

Signature: `disable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_accept_tr`

User definable method to add to ``accept_tr()``

Signature: `do_accept_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_begin_tr`

User definable method

Signature: `do_begin_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_seq_base.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_seq_base.do_end_tr`

Not implemented

Signature: `do_end_tr(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_seq_base.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.enable_recording`

Not implemented

Signature: `enable_recording(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.end_tr`

:param end_time: Simulation time at which the transaction

Signature: `end_tr(self, end_time=0, free_handle=True) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `end_time` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Simulation time at which the transaction |
| `free_handle` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | Parameter. |

Output: `None`

#### `uvm_reg_seq_base.get_accept_time`

:return: Accept time of transaction

Signature: `get_accept_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_seq_base.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_begin_time`

:return: Begin time of transaction

Signature: `get_begin_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_seq_base.get_end_time`

:return: End time of transaction

Signature: `get_end_time(self) -> int`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_reg_seq_base.get_event_pool`

Not implemented

Signature: `get_event_pool(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_initiator`

:return: initiator

Signature: `get_initiator(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_tr_handle`

Not implemented

Signature: `get_tr_handle(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_transaction_id`

:return: Transaction ID

Signature: `get_transaction_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.is_active`

Not implemented

Signature: `is_active(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_seq_base.is_recording_enabled`

Not implemented

Signature: `is_recording_enabled(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_seq_base.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.set_context`

Use this to link a new response transaction to the request transaction.

Signature: `set_context(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The request transaction |

Output: `None`

#### `uvm_reg_seq_base.set_id_info`

:param other: uvm_transaction with transaction_id

Signature: `set_id_info(self, other)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `other` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | uvm_transaction with transaction_id |

Output: `None`

#### `uvm_reg_seq_base.set_initiator`

:param initiator: initiator to set

Signature: `set_initiator(self, initiator)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `initiator` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | initiator to set |

Output: `None`

#### `uvm_reg_seq_base.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_seq_base.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_seq_base.set_transaction_id`

:param txn_id: Transaction ID

Signature: `set_transaction_id(self, txn_id)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `txn_id` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Transaction ID |

Output: `None`

#### `uvm_reg_seq_base.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_seq_base.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_seq_base.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_sequence`

Module: `pyuvm`

The uvm_sequence creates a series of sequence

### Constructor

Signature: `uvm_reg_sequence(self, name: 'str' = 'uvm_reg_sequence_inst')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_sequence_inst'` | Name of the object. Default is empty string. |

Output: `uvm_reg_sequence` instance

### Methods

#### `uvm_reg_sequence.body`

This function gets launched in a thread when you run start()

Signature: `body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_sequence.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_sequence.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_sequence.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_sequence.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_sequence.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_sequence.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.do_reg_item`

No description available.

Signature: `do_reg_item(self, rw: 'uvm_reg_item') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_sequence.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.finish_item`

No description available.

Signature: `finish_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_sequence.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_response`

No description available.

Signature: `get_response(self, transaction_id=None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `transaction_id` | `POSITIONAL_OR_KEYWORD` | `int` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_sequence.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.mirror_reg`

No description available.

Signature: `mirror_reg(self, rg: 'uvm_reg', check: 'uvm_check_e' = <uvm_check_e.UVM_NO_CHECK: 0>, path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `check` | `POSITIONAL_OR_KEYWORD` | `uvm_check_e` | `<uvm_check_e.UVM_NO_CHECK: 0>` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_sequence.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.peek_mem`

No description available.

Signature: `peek_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_sequence.peek_reg`

No description available.

Signature: `peek_reg(self, rg: 'uvm_reg', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_sequence.poke_mem`

No description available.

Signature: `poke_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_sequence.poke_reg`

No description available.

Signature: `poke_reg(self, rg: 'uvm_reg', value: 'uvm_reg_data_t', kind: 'str' = '', extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `kind` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_sequence.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.post_body`

This function gets launced AFTER the function body() is started

Signature: `post_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.pre_body`

This function gets launced BEFORE the function body() is started

Signature: `pre_body(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.read_mem`

No description available.

Signature: `read_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_sequence.read_reg`

No description available.

Signature: `read_reg(self, rg: 'uvm_reg', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_reg_sequence.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_sequence.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_sequence.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_sequence.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.start`

Launch this sequence on the sequencer. Seqr cannot be None.

Signature: `start(self, seqr=None, call_pre_post=True)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `seqr` | `POSITIONAL_OR_KEYWORD` | `object` | `None` | The sequencer to launch this sequence on. |
| `call_pre_post` | `POSITIONAL_OR_KEYWORD` | `bool` | `True` | If set to true (default), then pre_body and |

Output: `object`

#### `uvm_reg_sequence.start_item`

Sends an item to the sequencer and waits to be notified

Signature: `start_item(self, item)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The sequence item to send to the driver. |

Output: `object`

#### `uvm_reg_sequence.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_sequence.update_reg`

No description available.

Signature: `update_reg(self, rg: 'uvm_reg', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_sequence.write_mem`

No description available.

Signature: `write_mem(self, mem: 'uvm_mem', offset: 'uvm_reg_addr_t', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `required` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_reg_sequence.write_reg`

No description available.

Signature: `write_reg(self, rg: 'uvm_reg', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, prior: 'int' = -1, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_reg` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `prior` | `POSITIONAL_OR_KEYWORD` | `int` | `-1` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_reg_tlm_adapter`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_tlm_adapter(self, name: str = 'uvm_reg_tlm_adapter')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_tlm_adapter'` | Name of the object. Default is empty string. |

Output: `uvm_reg_tlm_adapter` instance

### Methods

#### `uvm_reg_tlm_adapter.bus2reg`

No description available.

Signature: `bus2reg(self, bus_item: pyuvm.uvm_sequence_item, rw: pyuvm.uvm_reg_bus_op) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `bus_item` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_item` | `required` | Parameter. |
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_bus_op` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_tlm_adapter.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_tlm_adapter.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_tlm_adapter.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_tlm_adapter.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_item`

No description available.

Signature: `get_item(self) -> pyuvm.uvm_reg_item`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_item`

#### `uvm_reg_tlm_adapter.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.reg2bus`

No description available.

Signature: `reg2bus(self, rw: pyuvm.uvm_reg_bus_op) -> pyuvm.uvm_sequence_item`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rw` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_bus_op` | `required` | Parameter. |

Output: `uvm_sequence_item`

#### `uvm_reg_tlm_adapter.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.set_item`

No description available.

Signature: `set_item(self, item: pyuvm.uvm_reg_item) -> None`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `item` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_item` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_tlm_adapter.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_tlm_adapter.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_tlm_adapter.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_tlm_adapter.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_tlm_adapter.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_transaction_order_policy`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_transaction_order_policy(self, name: 'str' = 'policy')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'policy'` | Name of the object. Default is empty string. |

Output: `uvm_reg_transaction_order_policy` instance

### Methods

#### `uvm_reg_transaction_order_policy.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_transaction_order_policy.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_transaction_order_policy.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.order`

No description available.

Signature: `order(self, q: 'list[uvm_reg_bus_op]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `q` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_bus_op]` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_transaction_order_policy.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_transaction_order_policy.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_transaction_order_policy.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_transaction_order_policy.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_transaction_order_policy.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_reg_write_only_cbs`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_reg_write_only_cbs(self, name: str = 'uvm_reg_write_only_cbs')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_reg_write_only_cbs'` | Name of the object. Default is empty string. |

Output: `uvm_reg_write_only_cbs` instance

### Methods

#### `uvm_reg_write_only_cbs.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_reg_write_only_cbs.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_write_only_cbs.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_write_only_cbs.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_reg_write_only_cbs.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_reg_write_only_cbs.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_reg_write_only_cbs.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_reg_write_only_cbs.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_reg_write_only_cbs.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_reg_write_only_cbs.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_status_e`

Module: `pyuvm`

Create a collection of name/value pairs.

### Enum Members

| Name | Value | Description |
|---|---|---|
| `UVM_IS_OK` | `0` | Enum member. |
| `UVM_NOT_OK` | `1` | Enum member. |
| `UVM_HAS_X` | `2` | Enum member. |

## Class `uvm_vreg`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg(self, name: 'str', n_bits: 'int')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object. Default is empty string. |
| `n_bits` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `uvm_vreg` instance

### Methods

#### `uvm_vreg.allocate`

No description available.

Signature: `allocate(self, n: 'int', mam: 'uvm_mem_mam', alloc: 'uvm_mem_mam_policy' = None) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `n` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `mam` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam` | `required` | Parameter. |
| `alloc` | `POSITIONAL_OR_KEYWORD` | `uvm_mem_mam_policy` | `None` | Parameter. |

Output: `None`

#### `uvm_vreg.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg.configure`

No description available.

Signature: `configure(self, parent: 'uvm_reg_block', mem: 'uvm_mem' = None, size: 'int' = 0, offset: 'uvm_reg_addr_t' = 0, incr: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_block` | `required` | Parameter. |
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `None` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `incr` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_vreg.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_access`

No description available.

Signature: `get_access(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_vreg.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_address`

No description available.

Signature: `get_address(self, idx: 'int', map: 'uvm_reg_map' = None) -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_vreg.get_block`

No description available.

Signature: `get_block(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_vreg.get_field_by_name`

No description available.

Signature: `get_field_by_name(self, name: 'str') -> 'uvm_vreg_field'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `uvm_vreg_field`

#### `uvm_vreg.get_fields`

No description available.

Signature: `get_fields(self, fields: 'list[uvm_vreg_field]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `fields` | `POSITIONAL_OR_KEYWORD` | `list[uvm_vreg_field]` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_vreg.get_incr`

No description available.

Signature: `get_incr(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_maps`

No description available.

Signature: `get_maps(self, maps: 'list[uvm_reg_map]') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `maps` | `POSITIONAL_OR_KEYWORD` | `list[uvm_reg_map]` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.get_memory`

No description available.

Signature: `get_memory(self) -> 'uvm_mem'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_mem`

#### `uvm_vreg.get_n_bytes`

No description available.

Signature: `get_n_bytes(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg.get_n_maps`

No description available.

Signature: `get_n_maps(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg.get_n_memlocs`

No description available.

Signature: `get_n_memlocs(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_offset_in_memory`

No description available.

Signature: `get_offset_in_memory(self, idx: 'int') -> 'uvm_reg_addr_t'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `uvm_reg_addr_t`

#### `uvm_vreg.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_reg_block'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_reg_block`

#### `uvm_vreg.get_region`

No description available.

Signature: `get_region(self) -> 'uvm_mem_region'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_mem_region`

#### `uvm_vreg.get_rights`

No description available.

Signature: `get_rights(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_vreg.get_size`

No description available.

Signature: `get_size(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.implement`

No description available.

Signature: `implement(self, mem: 'uvm_mem' = None, offset: 'uvm_reg_addr_t' = 0, incr: 'int' = 0) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `mem` | `POSITIONAL_OR_KEYWORD` | `uvm_mem` | `None` | Parameter. |
| `offset` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_addr_t` | `0` | Parameter. |
| `incr` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `None`

#### `uvm_vreg.is_in_map`

No description available.

Signature: `is_in_map(self, map: 'uvm_reg_map') -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `bool`

#### `uvm_vreg.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.peek`

No description available.

Signature: `peek(self, idx: 'int', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_vreg.poke`

No description available.

Signature: `poke(self, idx: 'int', value: 'uvm_reg_data_t', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_vreg.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.post_read`

No description available.

Signature: `post_read(self, idx: 'int', rdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `rdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.post_write`

No description available.

Signature: `post_write(self, idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.pre_read`

No description available.

Signature: `pre_read(self, idx: 'int', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.pre_write`

No description available.

Signature: `pre_write(self, idx: 'int', wdata: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdata` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.read`

No description available.

Signature: `read(self, idx: 'int', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_vreg.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.release_region`

No description available.

Signature: `release_region(self) -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg.write`

No description available.

Signature: `write(self, idx: 'int', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_vreg_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_vreg_cb` instance

### Methods

#### `uvm_vreg_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_vreg_cb.add_by_name`

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

#### `uvm_vreg_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_vreg_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_vreg_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_vreg_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_vreg_cb_iter` instance

### Methods

#### `uvm_vreg_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_vreg_cbs`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg_cbs(self, name: 'str' = 'uvm_vreg_cbs')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_vreg_cbs'` | Name of the object. Default is empty string. |

Output: `uvm_vreg_cbs` instance

### Methods

#### `uvm_vreg_cbs.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_vreg_cbs.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_cbs.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_cbs.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_cbs.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_cbs.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_cbs.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_cbs.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_vreg_cbs.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.post_read`

No description available.

Signature: `post_read(self, rg: 'uvm_vreg', idx: 'int', rdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `rdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cbs.post_write`

No description available.

Signature: `post_write(self, rg: 'uvm_vreg', idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cbs.pre_read`

No description available.

Signature: `pre_read(self, rg: 'uvm_vreg', idx: 'int', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cbs.pre_write`

No description available.

Signature: `pre_write(self, rg: 'uvm_vreg', idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rg` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cbs.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg_cbs.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg_cbs.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_cbs.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_cbs.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_vreg_field`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg_field(self, name: 'str' = 'uvm_vreg_field')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_vreg_field'` | Name of the object. Default is empty string. |

Output: `uvm_vreg_field` instance

### Methods

#### `uvm_vreg_field.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field.configure`

No description available.

Signature: `configure(self, parent: 'uvm_vreg', size: 'int', lsb_pos: 'int') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg` | `required` | Parameter. |
| `size` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `lsb_pos` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_access`

No description available.

Signature: `get_access(self, map: 'uvm_reg_map' = None) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |

Output: `str`

#### `uvm_vreg_field.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self) -> 'str'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `str`

#### `uvm_vreg_field.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_lsb_pos_in_register`

No description available.

Signature: `get_lsb_pos_in_register(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg_field.get_n_bits`

No description available.

Signature: `get_n_bits(self) -> 'int'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `int`

#### `uvm_vreg_field.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_parent`

No description available.

Signature: `get_parent(self) -> 'uvm_vreg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_vreg`

#### `uvm_vreg_field.get_register`

No description available.

Signature: `get_register(self) -> 'uvm_vreg'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_vreg`

#### `uvm_vreg_field.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.peek`

No description available.

Signature: `peek(self, idx: 'int', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_vreg_field.poke`

No description available.

Signature: `poke(self, idx: 'int', value: 'uvm_reg_data_t', parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

#### `uvm_vreg_field.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.post_read`

No description available.

Signature: `post_read(self, idx: 'int', rdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `rdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.post_write`

No description available.

Signature: `post_write(self, idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.pre_read`

No description available.

Signature: `pre_read(self, idx: 'int', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.pre_write`

No description available.

Signature: `pre_write(self, idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.read`

No description available.

Signature: `read(self, idx: 'int', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'tuple[uvm_status_e, uvm_reg_data_t]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `tuple[uvm_status_e, uvm_reg_data_t]`

#### `uvm_vreg_field.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg_field.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg_field.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field.write`

No description available.

Signature: `write(self, idx: 'int', value: 'uvm_reg_data_t', path: 'uvm_door_e' = <uvm_door_e.UVM_DEFAULT_DOOR: 3>, map: 'uvm_reg_map' = None, parent: 'uvm_sequence_base' = None, extension: 'uvm_object' = None, fname: 'str' = '', lineno: 'int' = 0) -> 'uvm_status_e'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `value` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `<uvm_door_e.UVM_DEFAULT_DOOR: 3>` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `None` | Parameter. |
| `parent` | `POSITIONAL_OR_KEYWORD` | `uvm_sequence_base` | `None` | Parameter. |
| `extension` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `None` | Parameter. |
| `fname` | `POSITIONAL_OR_KEYWORD` | `str` | `''` | Parameter. |
| `lineno` | `POSITIONAL_OR_KEYWORD` | `int` | `0` | Parameter. |

Output: `uvm_status_e`

## Class `uvm_vreg_field_cb`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg_field_cb(self, name: 'str' = 'uvm_callbacks')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_callbacks'` | Name of the object. Default is empty string. |

Output: `uvm_vreg_field_cb` instance

### Methods

#### `uvm_vreg_field_cb.add`

No description available.

Signature: `add(obj, cb, ordering: 'uvm_apprepend' = <uvm_apprepend.UVM_APPEND: 1>)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `ordering` | `POSITIONAL_OR_KEYWORD` | `uvm_apprepend` | `<uvm_apprepend.UVM_APPEND: 1>` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cb.add_by_name`

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

#### `uvm_vreg_field_cb.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field_cb.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field_cb.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cb.delete`

No description available.

Signature: `delete(obj, cb: 'uvm_callback') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cb.delete_by_name`

No description available.

Signature: `delete_by_name(name: 'str', cb: 'uvm_callback', root: 'uvm_component')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |
| `cb` | `POSITIONAL_OR_KEYWORD` | `uvm_callback` | `required` | Parameter. |
| `root` | `POSITIONAL_OR_KEYWORD` | `uvm_component` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cb.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field_cb.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field_cb.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cb.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get`

No description available.

Signature: `get()`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_all`

No description available.

Signature: `get_all(obj: 'uvm_object') -> 'list[uvm_callback]'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `list[uvm_callback]`

#### `uvm_vreg_field_cb.get_first`

No description available.

Signature: `get_first(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_last`

No description available.

Signature: `get_last(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_next`

No description available.

Signature: `get_next(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_prev`

No description available.

Signature: `get_prev(itr: 'int', obj: 'uvm_object') -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `itr` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `obj` | `POSITIONAL_OR_KEYWORD` | `uvm_object` | `required` | Parameter. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg_field_cb.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg_field_cb.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cb.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cb.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

## Class `uvm_vreg_field_cb_iter`

Module: `pyuvm`

No description available.

### Constructor

Signature: `uvm_vreg_field_cb_iter(self, obj: 'type[uvm_object] | uvm_object')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `obj` | `POSITIONAL_OR_KEYWORD` | `type[uvm_object] | uvm_object` | `required` | Parameter. |

Output: `uvm_vreg_field_cb_iter` instance

### Methods

#### `uvm_vreg_field_cb_iter.first`

No description available.

Signature: `first(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb_iter.get_cb`

No description available.

Signature: `get_cb(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb_iter.last`

No description available.

Signature: `last(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb_iter.next`

No description available.

Signature: `next(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

#### `uvm_vreg_field_cb_iter.prev`

No description available.

Signature: `prev(self) -> 'uvm_callback | None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `uvm_callback | None`

## Class `uvm_vreg_field_cbs`

Module: `pyuvm`

The most basic UVM object

### Constructor

Signature: `uvm_vreg_field_cbs(self, name: 'str' = 'uvm_vreg_field_cbs')`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `'uvm_vreg_field_cbs'` | Name of the object. Default is empty string. |

Output: `uvm_vreg_field_cbs` instance

### Methods

#### `uvm_vreg_field_cbs.callback_mode`

No description available.

Signature: `callback_mode(self, on: 'bool | None' = None)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `on` | `POSITIONAL_OR_KEYWORD` | `bool | None` | `None` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cbs.clone`

:return: A new object with the same name and data as this object.

Signature: `clone(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.compare`

:param rhs: The object being compared.

Signature: `compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field_cbs.convert2string`

:return: The result of ``__str__()``

Signature: `convert2string(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.copy`

:param rhs: The object to copy from

Signature: `copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field_cbs.create`

:return: new object from factory

Signature: `create(name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cbs.do_compare`

:param rhs: The object being compared.

Signature: `do_compare(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object being compared. |

Output: `object`

#### `uvm_vreg_field_cbs.do_copy`

:param rhs: The object to copy from

Signature: `do_copy(self, rhs)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `rhs` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | The object to copy from |

Output: `object`

#### `uvm_vreg_field_cbs.do_execute_op`

Not implemented.

Signature: `do_execute_op(self, op)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `op` | `POSITIONAL_OR_KEYWORD` | `object` | `required` | Parameter. |

Output: `object`

#### `uvm_vreg_field_cbs.do_pack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.do_print`

not implemented. Use __str__() and print()

Signature: `do_print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.do_record`

Not implemented as we are not in a simulator

Signature: `do_record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.do_unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `do_unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_active_policy`

Not implemented.

Signature: `get_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_full_name`

:return: The full path and name of the object

Signature: `get_full_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_inst_id`

:return: The python ID which fits the bill for what the ID

Signature: `get_inst_id(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_name`

:return: String with name of uvm_object.

Signature: `get_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_object_type`

Not implemented because Python can implement the factory without

Signature: `get_object_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_type`

Not implemented because Python can implement the factory without

Signature: `get_type(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_type_name`

:return: Returns the type's ``__name__`` magic variable

Signature: `get_type_name(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.get_uvm_seeding`

Not implemented

Signature: `get_uvm_seeding(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.is_enabled`

No description available.

Signature: `is_enabled(self) -> 'bool'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `bool`

#### `uvm_vreg_field_cbs.pack`

Not implemented. There are Pythonic solutions to this.

Signature: `pack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.pack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.pack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.pack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `pack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.pop_active_policy`

Not implemented.

Signature: `pop_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.post_read`

No description available.

Signature: `post_read(self, field: 'uvm_vreg_field', idx: 'int', rdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `field` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg_field` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `rdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cbs.post_write`

No description available.

Signature: `post_write(self, field: 'uvm_vreg_field', idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map', status: 'uvm_status_e') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `field` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg_field` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |
| `status` | `POSITIONAL_OR_KEYWORD` | `uvm_status_e` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cbs.pre_read`

No description available.

Signature: `pre_read(self, field: 'uvm_vreg_field', idx: 'int', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `field` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg_field` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cbs.pre_write`

No description available.

Signature: `pre_write(self, field: 'uvm_vreg_field', idx: 'int', wdat: 'uvm_reg_data_t', path: 'uvm_door_e', map: 'uvm_reg_map') -> 'None'`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `field` | `POSITIONAL_OR_KEYWORD` | `uvm_vreg_field` | `required` | Parameter. |
| `idx` | `POSITIONAL_OR_KEYWORD` | `int` | `required` | Parameter. |
| `wdat` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_data_t` | `required` | Parameter. |
| `path` | `POSITIONAL_OR_KEYWORD` | `uvm_door_e` | `required` | Parameter. |
| `map` | `POSITIONAL_OR_KEYWORD` | `uvm_reg_map` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cbs.print`

Not implemented. Use __str__() and print()

Signature: `print(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.push_active_policy`

Not implemented.

Signature: `push_active_policy(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.record`

Not implemented.

Signature: `record(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.reseed`

Not implemented

Signature: `reseed(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.set_local`

Not implemented use Python getattr and setattr.

Signature: `set_local(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `None`

#### `uvm_vreg_field_cbs.set_name`

:param name: Name of the object

Signature: `set_name(self, name)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `name` | `POSITIONAL_OR_KEYWORD` | `str` | `required` | Name of the object |

Output: `None`

#### `uvm_vreg_field_cbs.set_uvm_seeding`

Not implemented

Signature: `set_uvm_seeding(self, enable)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| `enable` | `POSITIONAL_OR_KEYWORD` | `bool` | `required` | Parameter. |

Output: `None`

#### `uvm_vreg_field_cbs.sprint`

Not implemented. use __str__() and print()

Signature: `sprint(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.unpack`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.unpack_bytes`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_bytes(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.unpack_ints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_ints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

#### `uvm_vreg_field_cbs.unpack_longints`

Not implemented. There are Pythonic solutions to this.

Signature: `unpack_longints(self)`

Inputs

| Name | Kind | Type | Default | Description |
|---|---|---|---|---|
| (none) | - | - | - | No input parameters. |

Output: `object`

