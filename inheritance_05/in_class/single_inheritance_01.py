"""
    1. Single Inheritance
Create two classes named Animal and Dog.
Animal with a single public method eat() that returns: "eating…"
Dog with a single public method bark() that returns: "barking…"
Dog should inherit from Animal.
"""

class Animal:

    @staticmethod
    def eat():
        return "eating..."

class Dog(Animal):

    @staticmethod
    def bark():
        return "barking..."

my_dog = Dog()
print(my_dog.bark())
print(my_dog.eat())