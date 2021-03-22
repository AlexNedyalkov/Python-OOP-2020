'''
    1. Custom Range
Create a class called custom_range that receives start and end upon initialization. Implement the __iter__ and __next__
methods, so the iterator returns the numbers from the start to the end (inclusive).
'''

class custom_range():


    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.custom_range_id = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.custom_range_id += 1
        if self.start + self.custom_range_id == self.end + 1:
            raise StopIteration
        return self.start + self.custom_range_id



one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
