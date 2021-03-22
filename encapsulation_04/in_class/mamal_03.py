"""
Create a class called Mammal. Upon initialization it should receive a name, type and sound.
Create private class attribute called kingdom and set it to be "animals". Create three more instance methods:
    • make_sound() - returns a string in the format "{name} makes {sound}"
    • get_kingdom() - returns the private kingdom attribute
    • info() - returns a string in the format "{name} is of type {type}"
"""
class Mammal:

    def __init__(self, name: str, type: str, sound: str):
        self.name: str = name
        self.type: str = type
        self.sound: str = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())