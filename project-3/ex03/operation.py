from utils import format_cents


class Operation:
    def __init__(self, cents: int, description: str) -> None:
        """a function that initializes the class Operation with cents and description"""
        if cents == 0 or not isinstance(cents, int):
            raise ValueError("invalid value for cents")
        if not isinstance(description, str):
            raise ValueError("invalid value for description")
        self.cents = cents
        self.description = description
        self.operation_type = "credit" if cents > 0 else "debit"

    def __repr__(self):
        """a function that show a more descritive Operation class"""
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type}', description='{self.description}')"

    def __str__(self):
        """a fuction that show a more friendly way the class"""
        return f"{format_cents(self.cents)} {self.description}"
