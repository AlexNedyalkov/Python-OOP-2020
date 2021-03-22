"""
    2. Integer
Create a class called Integer. Upon initialization it should receive a single parameter value (int).
It should have 4 methods:
    • from_float(value) - creates a new instance by flooring the provided floating number.
    If the value is not a float return a message "value is not a float"
    • from_roman(value) – creates a new instance by converting the roman number (as string) to an integer
    • from_string(value) - creates a new instance by converting the string to an integer
     (if the value cannot be converted, return a message "wrong type")
    • add(integer:Integer) – adds the values of the two instances and returns the result
    (if the integer is not an instance of Integer, return the message "number should be an Integer instance")
"""

class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if type(value) != float:
            return "value is not a float"
        return Integer(int(value))

    @classmethod
    def from_roman(cls, value: str):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        return Integer(roman[value])

    @classmethod
    def from_string(cls, value: str):
        if type(value) == str:
            return Integer(int(value))
        return "wrong type"

    def add(self, integer):
        self.value += integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")
first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))


