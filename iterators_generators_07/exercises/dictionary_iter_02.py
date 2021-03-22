class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary
        self.__counter = -1
        self.__keys = list(dictionary.keys())

    @property
    def dictionary(self):
        return self

    @dictionary.setter
    def dictionary(self, new_dictionary: dictionary):
        self.__dictionary = new_dictionary

    def __iter__(self):
        return self

    def __next__(self):
        self.__counter += 1
        if self.__counter == len(self.__keys):
            raise StopIteration
        else:
            return self.__keys[self.__counter], self.__dictionary[self.__keys[self.__counter]]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)