import time

def exec_time(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        stop = time.time()
        return stop - start
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))