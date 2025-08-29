import pytest
from utils import format_cents


@pytest.mark.parametrize(
    "value, formated",
    [
        (11_222_00, "[+] R$ 11.222,00"),
        (-11_222_00, "[-] R$ 11.222,00"),
        (150, "[+] R$ 1,50"),
        (123456, "[+] R$ 1.234,56"),
        (-987654, "[-] R$ 9.876,54"),
    ],
)
def test_diff_values_format_cents(value: int, formated: str) -> None:
    assert format_cents(value) == formated


def test_input_error() -> None:
    with pytest.raises(ValueError):
        format_cents("a")  # type: ignore
