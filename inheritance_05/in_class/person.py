class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def get_info(self):
        return f"{self.first_name} is {self.age} years old."

class Student(Person):
    def __init__(self, first_name, age, student_id):
        super().__init__(first_name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

    def get_student_info(self):
        return super().get_info()[:-1] + " and the student id is " + str(self.get_id())

# Create an object of the superclass
person = Person("John", 25)
print(person.get_info())
# returns 'John is 25 years old.'

# Create an object of the subclass
student = Student("Leo", 20, 10035464)
print(student.get_info())
# returns 'Leo is 20 years old.'
print(student.get_id())
# returns 10035464
print(student.get_student_info())