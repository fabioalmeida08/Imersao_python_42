import sys


def main() -> None:
    """
    function that try to read a file that is passed as argument and print the contents of the file
    """
    try:
        with open(sys.argv[1]) as f:
            print(f.read())
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório")
    except Exception as e:
        print(f"Erro inesperado: {type(e).__name__}")


if __name__ == "__main__":
    main()
