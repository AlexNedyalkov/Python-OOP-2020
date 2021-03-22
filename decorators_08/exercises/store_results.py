class store_results:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, *args, **kwargs):
        result = self.func(*args)
        with open('result.txt', 'a') as f:
            f.write(f"Function {self.func.__name__} was called. Result: {result}\n")



@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

with open('result.txt', 'w') as f:
    pass

add(2, 2)
mult(6, 4)
add(2, 2)
add(2, 2)
add(2, 2)
