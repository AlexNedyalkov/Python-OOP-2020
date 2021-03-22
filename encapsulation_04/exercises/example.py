class A:

    def __init__(self):
        self.__private = "private"

a = A()
a.__private = "changed"
print(a.__private)