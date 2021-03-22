from project.product import Product

class Beverage(Product):

    def __init__(self, name, price, ml):
        super().__init__(name, price)
        self._milliliters  = ml

    @property
    def milliliters(self):
        return self._milliliters

#     @milliliters.setter
#     def milliliters(self, new_ml):
#         self._milliliters = new_ml
#
# my_beverage = Beverage("Choko", 5, 10)
# print(my_beverage.__dict__)
# my_beverage._name = "Doko"
# print(my_beverage.__dict__)
# my_beverage.milliliters = 25
# print(my_beverage.__dict__)