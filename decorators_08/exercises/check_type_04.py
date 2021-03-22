def generic(parameter):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return wrapper

def type_check(_type):
    def wrapper(func):
        def wrapped(arg):
            if isinstance(arg, _type):
                return func(arg)

            return "Bad Type"

        return wrapped
    return wrapper


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))