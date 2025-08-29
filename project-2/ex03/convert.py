import sys

def main () -> None:
    """function that try to convert a arg to a float and if fail print a custom error message"""
    try:
        print(float(sys.argv[1]))
    except ValueError:
        print("conversion impossible")
    except IndexError:
        print("invalid number of args")

if __name__ == "__main__":
    main()
