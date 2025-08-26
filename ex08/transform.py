import sys


def square_even_numbers(lst: list[str]) -> list[int]:
    return [int(x) ** 2 for x in lst if int(x) % 2 == 0]


if __name__ == "__main__":
    try:
        print(square_even_numbers(sys.argv[1].split(" ")))
    except IndexError:
        print("missing argument")
