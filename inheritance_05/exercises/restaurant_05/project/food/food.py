from project.product import Product

class Food(Product):
    def __init__(self, name, price, gr):
        super().__init__(name, price)
        self._grams = gr

    @property
    def grams(self):
        return self._grams