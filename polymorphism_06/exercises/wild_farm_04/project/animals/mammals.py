from polymorphism_06.exercises.wild_farm_04.project.animals.animal import Mammal, Animal, Bird
from polymorphism_06.exercises.wild_farm_04.project.animals.birds import Owl, Hen

from polymorphism_06.exercises.wild_farm_04.project.food import Food, Meat, Vegetable, Seed, Fruit


class Mouse(Mammal):

    food_coefficient = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.eat_food(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Dog(Mammal):

    food_coefficient = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.eat_food(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Cat(Mammal):

    food_coefficient = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.eat_food(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):

    food_coefficient = 1.00

    def make_sound(self):
        return "ROAR"

    def feed(self, food):
        if isinstance(food, Meat):
            self.eat_food(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
veg.quantity = 10
print(veg.quantity)
print(veg.__dict__)
fruit = Fruit(5)

meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)