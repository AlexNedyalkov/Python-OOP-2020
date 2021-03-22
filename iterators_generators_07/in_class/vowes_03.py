class vowels:
    def __init__(self, my_string: str):
        self.my_string = my_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.my_string):
            raise StopIteration
        else:
            if self.my_string[self.index - 1].lower() in ('a', 'e','i', 'o', 'u'):
                return self.my_string[self.index - 1]
            else:
                return self.__next__()



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
