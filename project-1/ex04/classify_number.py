import sys


def is_positive(nbr: int) -> bool:
    """return boolean value if the number is positive"""
    return nbr > 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid number of arguments")
    else:
        print(is_positive(int(sys.argv[1])))
