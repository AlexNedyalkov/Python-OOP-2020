class sequence_repeat:

    def __init__(self, sequence:str, number):
        self.sequence = sequence
        self.__org_sequence = sequence
        self.number = number
        self.__index = -1
        self.__counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        self.__counter += 1
        if self.__counter == self.number:
            raise StopIteration
        else:
            if len(self.sequence) == self.__index:
                self.__index = 0
            return self.sequence[self.__index]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')