import sys


def downcase_it(string: str) -> str:
    """put all letters from the string to lowercase"""
    return string.lower()


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        print(downcase_it(sys.argv[i]))
