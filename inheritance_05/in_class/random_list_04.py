import random

"""
    4. Random List
Create a RandomList class that has all the functionality of a List.
Add additional function that returns and removes a random element from the list.
    • Public method: get_random_element()
"""
class RandomList(list):

    def get_random_element(self):

        pass
        element_to_remove = random.choice(self)
        self.remove(element_to_remove)
        return element_to_remove



my_random_list = RandomList([1,22,31,42,59])
my_random_list.get_random_element()
print(my_random_list)