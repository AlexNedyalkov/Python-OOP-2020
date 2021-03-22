'''
Create a class called ImageArea which will store the width and the height of an image. Create a method called get_area()
 which will return the area of the image. We have to also implement all the magic methods for comparison of two image
 areas (>, >=, <, <=, ==, !=) which will compare their areas
'''

class ImageArea:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__height * self.__width

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)