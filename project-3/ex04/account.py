from utils import format_cents
from operation import Operation


class Account:
    def __init__(self, accont_id: int, cpf: str) -> None:
        """a function that initializes a class Account"""
        if not isinstance(accont_id, int):
            raise ValueError("invalid type for account_id")
        if not isinstance(cpf, str):
            raise ValueError("invalid type for cpf")
        self.account_id: int = accont_id
        self.cpf: str = cpf
        self.__balance: int = 0
        self.__operations: list[Operation] = []

    def deposit(self, amount: int, description: str) -> None:
        """a function that add a amount to the Account class balance atribute"""
        if not amount > 0:
            raise ValueError("valor deve ser > 0")
        self.__balance += amount
        op = Operation(amount, description)
        self.__operations.append(op)

    def withdraw(self, amount: int, description: str) -> None:
        """a function that withdraw a certain amount from the account balance atribute"""
        if not amount > 0:
            raise ValueError("valor deve ser > 0")
        self.__balance -= amount
        op = Operation(amount, description)
        self.__operations.append(op)

    def statement(self) -> None:
        """a function that show a list of record of operations that the account done"""
        for i in self.__operations:
            print(i)
        print(self.__get_balance())

    def __repr__(self) -> str:
        """a function that show a more descritive Account class"""
        return f"Account({self.account_id}, '{self.cpf}')"

    def __str__(self) -> str:
        """a function that show a more friendly way the Account class"""
        return f"Account: {self.account_id}\n{self.__get_balance()}"

    def __get_balance(self) -> str:
        """a function that get the balance from the account and show formated that Balance: account_balance"""
        return f"Balance: {format_cents(self.__balance)}"
