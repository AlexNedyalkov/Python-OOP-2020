"""
Attributes
Public attribute name: string
Public attribute gender: string
Public attribute age: number
Methods
__init__(name, gender, age) - set all the attributes to the given ones
get_needs() - returns the number 45 (amount of money needed to tend the animal)
__repr__() - returns string representation of the tiger in the format: "Name: {name}, Age: {age}, Gender: {gender}"
"""
class Tiger:

    def __init__(self, name: str, gender: str, age: int):
        self.name: str = name
        self.gender: str = gender
        self.age:int = age

    @staticmethod
    def get_needs():
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

