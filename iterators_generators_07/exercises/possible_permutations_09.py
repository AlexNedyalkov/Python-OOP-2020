from itertools import permutations

def possible_permutations(my_list):
    my_permutations = list((permutations(my_list)))
    for permutation in my_permutations:
        yield list(permutation)

[print(n) for n in possible_permutations([1, 2, 3])]
