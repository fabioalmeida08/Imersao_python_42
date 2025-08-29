import pytest
import password_validador


@pytest.mark.parametrize(
    "password, expected",
    [
        ("senha123@", False),
        ("SENHA123@", False),
        ("Senha@abc", False),
        ("Senha1234", False),
        ("Senha@ 123", False),
        ("S@1a", False),
        ("Senha@1234567890A", False),
        ("Senha@123", True),
        ("A1@bcdefgh", True),
        ("Zz9!Yy8&", True),
        ("A1@bcdef", True),
        ("Abcdef@123456789", True),
    ],
)

def test_password_tester_validator(password: str, expected: bool) -> None:
    assert password_validador.is_valid_password(password) == expected
