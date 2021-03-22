"""
Create a class called Point. Upon initialization it should receive x and y (numbers). Create 3 instance methods:
    • set_x(new_x) - changes the x value of the point
    • set_y(new_y) - changes the y value of the point
    • distance(x, y) - returns the distance between the point and the provided coordinates
"""
class Point:

    def __init__(self, x:int, y:int):
        self.x:int = x
        self.y:int = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**(1/2)

# p = Point(2, 4)
# p.set_x(3)
# p.set_y(5)
# print(p.distance(10, 2))