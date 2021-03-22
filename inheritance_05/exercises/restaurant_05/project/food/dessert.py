from project.food.food import Food

class Dessert(Food):

    def __init__(self, name, price, gr, calories):
        super().__init__(name, price, gr)
        self._calories = calories

    @property
    def calories(self):
        return self._calories