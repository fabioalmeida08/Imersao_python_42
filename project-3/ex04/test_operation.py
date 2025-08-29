from operation import Operation
import pytest


def test_initialize_class_operation() -> None:
    op = Operation(1234, "ATM Deposit")
    assert op.cents == 1234
    assert op.description == "ATM Deposit"


def test_invalid_value_for_cents() -> None:
    with pytest.raises(ValueError):
        op = Operation(0, "ATM Deposit")


def test_operation_type_value_for_credit() -> None:
    op = Operation(12, "ATM Deposit")
    assert op.operation_type == "credit"


def test_operation_type_value_for_debit() -> None:
    op = Operation(-12, "ATM Deposit")
    assert op.operation_type == "debit"


def test_invalid_value_for_cents_raises_error() -> None:
    with pytest.raises(ValueError):
        Operation("a", "atm")  # type: ignore


def test_invalid_value_for_description_raises_error() -> None:
    with pytest.raises(ValueError):
        Operation(1234, 1234)  # type: ignore

def test_repr_validation() -> None:
    op = Operation(12, "ATM Deposit")
    assert repr(op) == "Operation(cents=12, operation_type='credit', description='ATM Deposit')"

def test_str_validation() -> None:
    op = Operation(12, "ATM Deposit")
    assert "ATM Deposit" in str(op)
