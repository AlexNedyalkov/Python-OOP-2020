def multiply(function, multiplier):
    def wrapper():
        function() * multiplier
    return wrapper

@multiply(3)
def add_ten():
    return 10

print(add_ten())


