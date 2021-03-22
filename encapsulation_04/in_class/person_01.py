class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        if new_age >= 18 and isinstance(new_age, int):
            self.__age = new_age
        else:
            print("Wrong age")





person = Person("George", 32)

print(person.name)
print(person.age)
person.name = "Pesho"
print(person.name)
person.age = 119
print(person.age)

