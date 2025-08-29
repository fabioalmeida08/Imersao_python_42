import pytest
from account import Account


def test_initialize_class_account_operation() -> None:
    ac = Account(1234, "197.210.840-93")
    assert ac.account_id == 1234
    assert ac.cpf == "197.210.840-93"


def test_invalid_value_for_account_id_raises_error() -> None:
    with pytest.raises(ValueError, match="invalid type for account_id"):
        ac = Account("a", "atm")  # type: ignore


def test_invalid_value_for_account_cpf_raises_error() -> None:
    with pytest.raises(ValueError, match="invalid type for cpf"):
        ac = Account(111, 111)  # type: ignore


def test_invalid_value_for_deposit() -> None:
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        ac = Account(1234, "197.210.840-93")
        ac.deposit(0, "testing 0")


def test_invalid_value_for_withdraw() -> None:
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        ac = Account(1234, "197.210.840-93")
        ac.withdraw(0, "testing 0")
