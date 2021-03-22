class take_skip:

    def __init__(self, step: int, count: int):
        self.__step = step
        self.__count = count
        self.__number = 0 - self.__step
        self.counter = 0

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, new_step):
        self.__step = new_step

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, new_count):
        self.__count = new_count

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > self.count:
            raise StopIteration
        else:
            self.__number += self.step
            return self.__number

numbers = take_skip(10, 5)
for number in numbers:
    print(number)