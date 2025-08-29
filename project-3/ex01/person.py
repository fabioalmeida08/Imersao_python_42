class Person:
    def __init__(self, name: str, age: int):
        """a function that initializes de Person class"""
        self.name = name
        self.age = age

    def birthday(self) -> None:
        """increment the person age by 1 year"""
        self.age += 1
