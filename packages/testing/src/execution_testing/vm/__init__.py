"""Ethereum Virtual Machine related definitions and utilities."""

from .bytecode import Bytecode
from .evm_types import EVMCodeType
from .helpers import MemoryVariable, call_return_code
from .opcodes import (
    Macro,
    Macros,
    Opcode,
    OpcodeCallArg,
    Opcodes,
    UndefinedOpcodes,
    arb_block_number,
)

# Ergonomic alias for the commonly used Opcodes enum
Op = Opcodes

__all__ = (
    "Bytecode",
    "EVMCodeType",
    "Macro",
    "Macros",
    "MemoryVariable",
    "Op",
    "Opcode",
    "OpcodeCallArg",
    "Opcodes",
    "UndefinedOpcodes",
    "arb_block_number",
    "call_return_code",
)
