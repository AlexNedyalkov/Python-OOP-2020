def tags(arg):
    def wrapped(func):
        def wrapper(*args):
            return f'<{arg}>' + func(*args) + f'</{arg}>'
        return wrapper
    return wrapped

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
