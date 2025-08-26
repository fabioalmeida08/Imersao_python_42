import sys


def downcase_it(string: str) -> str:
    """put all letters from the string to lowercase"""
    return string.lower()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(None)
    else:
        for arg in sys.argv[1:]:
            print(downcase_it(arg))
