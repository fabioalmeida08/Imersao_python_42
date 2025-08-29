from utils import format_cents
from enum import Enum

class OperationType(Enum):
    """enum to represent credit and debit"""
    CREDIT = 'credit'
    DEBIT = 'debit'

class Operation:
    def __init__(self, cents: int, description: str) -> None:
        """a function that initialize a operation class"""
        if cents == 0 or not isinstance(cents, int):
            raise ValueError("invalid value for cents")
        if not isinstance(description, str):
            raise ValueError("invalid value for description")
        self.cents = cents
        self.description = description
        self.operation_type: OperationType = OperationType.CREDIT if cents > 0 else OperationType.DEBIT

    def __repr__(self) -> str:
        """a function that show a more descritive Operation class"""
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type.value}', description='{self.description}'"

    def __str__(self) -> str:
        """a fuction that show a more friendly way the class"""
        return f"{format_cents(self.cents)} ({self.description})"
