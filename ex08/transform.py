import sys


def square_even_numbers(lst: list[int]) -> list[int]:
    """receive a list of integers and return a new list of the square of even numbers in the list"""
    return [x**2 for x in lst if x % 2 == 0]


if __name__ == "__main__":
    try:
        print(square_even_numbers(list(map(int, sys.argv[1].split(" ")))))
    except IndexError:
        print("missing argument")
