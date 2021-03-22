'''
Animal - name (string), weight (float), food_eaten (attribute, 0 upon initialization) - abstract class
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight
        self.food_eaten = 0

    @property
    def name(self):
        return self.__name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def eat_food(self, food):
        self.weight += food.quantity * self.food_coefficient
        self.food_eaten += food.quantity

class Bird(Animal, ABC):

    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.__wing_size = wing_size

    @property
    def wing_size(self):
        return self.__wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):

    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.__living_region = living_region

    @property
    def living_region(self):
        return self.__living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"




