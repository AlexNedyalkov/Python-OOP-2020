"""
Class Caretaker
Attributes
Public attribute name: string
Public attribute age: number
Public attribute salary: number
Methods
__init__(name, age, salary) - set all the attributes to the given ones
__repr__() - returns string representation of the caretaker in the format: "Name: {name}, Age: {age}, Salary: {salary}"
"""


class Caretaker:

    def __init__(self, name: str, age: int, salary: int):
        self.name: str = name
        self.age: int = age
        self.salary: int = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

