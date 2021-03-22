"""
    2. Multiple Inheritance
Create three classes named Person, Employee and Teacher.
Person with a single public method sleep() that returns: "sleeping..."
Employee with a single public method get_fired() that returns: "fired..."
Teacher with a single public method teach() that returns: "teaching..."
Teacher should inherit from Person and Employee.
"""
class Person:

    @staticmethod
    def sleep():
        return "sleeping..."

class Employee():

    @staticmethod
    def get_fired():
        return "fired..."

class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."