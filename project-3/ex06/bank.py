from account import Account
class Bank:
    def __init__(self):
        """initialize the Bank class"""
        self.__accounts: list[Account] = []

    def add_account(self, account: Account):
        """add a Account class to the accounts array"""
        self.__accounts.append(account)

    def get_account_by_cpf(self, cpf: str):
        """search for cpf on the accounts atribute, if not found return a None"""
        for acc in self.__accounts:
            if cpf == acc.cpf:
                return acc
            return None

    def transfer(self, source_account: int, destination_account: int, value: int, description: str):
        
        pass
