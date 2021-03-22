def make_bold(func):
    def wrapper(*args):
        return f'<b>{func(*args)}</b>'
    return wrapper

def make_italic(func):
    def wrapper(*args):
        return f'<i>{func(*args)}</i>'
    return wrapper

def make_underline(func):
    def wrapper(*args):
        return f'<u>{func(*args)}</u>'
    return wrapper

@make_underline
@make_italic
@make_bold
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_underline
@make_italic
@make_bold
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))