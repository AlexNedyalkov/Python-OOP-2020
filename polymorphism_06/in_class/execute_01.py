'''
Create a function called execute that receives a function as first argument and then all the other arguments
Return the result of the execution of the passed function with that arguments
Submit only the execute function in the judge system
'''

def execute(func, *args):
    return func(*args)

def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
