from polymorphism_06.exercises.wild_farm_04.project.animals.animal import Bird, Animal
from polymorphism_06.exercises.wild_farm_04.project.food import Food, Meat, Vegetable, Seed

class Hen(Bird):

    food_coefficient = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.eat_food(food)

class Owl(Bird):

    food_coefficient = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.eat_food(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


