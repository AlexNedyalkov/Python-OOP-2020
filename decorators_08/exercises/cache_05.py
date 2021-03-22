def cache(func):
    log = {}
    def wrapper(arg):
        if not (arg in log):
            log[arg] = func(arg)
        return func(arg)
    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

fibonacci(4)
print(fibonacci.log)