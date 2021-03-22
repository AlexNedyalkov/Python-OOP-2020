def solution():

    def integers():
        number = 0
        while True:
            number += 1
            yield number

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        my_list = []
        for num in seq:
            if len(my_list) < n:
                my_list.append(num)
            else:
                return my_list

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))