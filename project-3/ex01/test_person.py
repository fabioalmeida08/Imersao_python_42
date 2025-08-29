import pytest
from person import Person


def test_person_initialization() -> None:
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30


def test_person_birthdaymethod() -> None:
    p = Person("Alice", 30)
    p.birthday()
    assert p.age == 31


def test_person_age_type_error() -> None:
    with pytest.raises(TypeError):
        p = Person("Dave", "a")  # type:ignore
        p.birthday()
