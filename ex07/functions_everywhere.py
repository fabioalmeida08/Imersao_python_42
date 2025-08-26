import sys


def shrink(string: str) -> None:
    """print the fist 8 letters from the string"""
    print(string[:8])


def enlarge(string: str) -> None:
    """fill the string with Z's if the string has less than 8 letters"""
    print(string.ljust(8, "Z"))


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        if len(sys.argv[i]) > 8:
            shrink(sys.argv[i])
        elif len(sys.argv[i]) == 8:
            print(sys.argv[i])
        else:
            enlarge(sys.argv[i])
