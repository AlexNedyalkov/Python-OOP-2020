"""
    3. Hierarchical Inheritance
Create three classes named Animal, Dog and Cat.
Animal with a single public method eat() that returns: "eating..."
Dog with a single public method bark() that returns: "barking..."
Cat with a single public method meow() that returns: "meowing..."
Dog and Cat should inherit from Animal.
"""
class Animal:

    def eat(self):
        return "eating..."


class Dog(Animal):

    def bark(self):
        return "barking..."


class Cat(Animal):

    def meow(self):
        return "meowing..."
