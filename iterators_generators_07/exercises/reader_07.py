# def read_next(*args):
#     for seq in args:
#         for el in seq:
#             yield el

def read_next(*args):
    for seq in args:
        for item in seq:
            yield item

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
