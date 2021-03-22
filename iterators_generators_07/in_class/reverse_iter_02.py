'''
    2. Reverse Iter
Create a class called reverse_iter which should receive an iterable upon initialization.
Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
'''

class reverse_iter:
    def __init__(self, my_iteralble):
        self.my_iteralble = my_iteralble
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.my_iteralble):
            raise StopIteration
        else:
            return self.my_iteralble[len(self.my_iteralble) - self.count]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)