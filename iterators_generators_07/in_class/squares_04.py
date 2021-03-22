def squares(number: int):
    counter = 0
    while counter < number:
        counter += 1
        yield counter ** 2


print(list(squares(5)))