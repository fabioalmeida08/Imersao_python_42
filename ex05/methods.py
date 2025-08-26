import sys

if __name__ == "__main__":
    print(f"São maísculas? {sys.argv[1].isupper()}")
    print(f"É númerico? {sys.argv[1].isnumeric()}")
    print(f"É ascii? {sys.argv[1].isascii()}")
    print(f"É alfanumérico? {sys.argv[1].isalnum()}")
