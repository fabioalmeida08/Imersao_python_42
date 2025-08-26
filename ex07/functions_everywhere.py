import sys


def shrink(string: str) -> None:
    """print the fist 8 letters from the string"""
    print(string[:8])


def enlarge(string: str) -> None:
    """fill the string with Z's if the string has less than 8 letters"""
    print(string.ljust(8, "Z"))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("None")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) == 8:
                print(arg)
            else:
                enlarge(arg)
