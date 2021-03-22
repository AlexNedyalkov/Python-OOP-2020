from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.__quantity = quantity

    # @property
    # def quantity(self):
    #     return self.__quantity
    #
    # @quantity.setter
    # def quantity(self, new_quantity):
    #     self.__quantity = new_quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity=quantity)

class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity=quantity)

class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity=quantity)

class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity=quantity)