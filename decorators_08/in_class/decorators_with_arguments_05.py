# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(argument_01, arguments_02):
#         print(f'My arguments are {argument_01} and {arguments_02}')
#         function(argument_01.upper(), arguments_02.upper())
#     return wrapper_accepting_arguments
#
# @decorator_with_arguments
# def cities(city_one, city_two):
#     print(f"Cities I love are {city_one} and {city_two}")
#
# cities("Sofia", "Burgas")


def upper_case_decorator(function):

    def wrapper():
        return function().upper()

    return wrapper

def split_string(function):

    def wrapper():
        return function().split()
    return wrapper

@split_string
@upper_case_decorator
def say_hi():
    return 'Hola mi amigo'

print(say_hi())

