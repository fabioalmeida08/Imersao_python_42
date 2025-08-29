import re


def is_valid_password(password: str) -> bool:
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])\S{8,16}$"
    return re.match(pattern, password, re.VERBOSE) is not None
