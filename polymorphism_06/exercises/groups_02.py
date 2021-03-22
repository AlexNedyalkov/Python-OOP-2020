'''
Create a class called Person. Upon initialization it will receive a name (str) and a surname (str).
Create another class called Group. Upon initialization it should receive a name (str) and people (list of Person instances).
Implement the needed magic methods, so the test code below works
'''
class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name: str, people_list: list):
        self.name = name
        self.people = people_list

    def __str__(self):
        members_names = [member.__str__() for member in self.people]
        members = (', ').join(members_names)
        return f'Group {self.name} with member {members}'

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_group = Group(self.name + other.name, [])
        for member in self.people:
            new_group.people.append(member)
        for member in other.people:
            new_group.people.append(member)
        return new_group

    def __getitem__(self, item):
        return f'Person {item}: ' + str(self.people[item])

if __name__ == '__main__':
    p0 = Person('Aliko', 'Dangote')
    p1 = Person('Bill', 'Gates')
    p2 = Person('Warren', 'Buffet')
    p3 = Person('Elon', 'Musk')
    p4 = p2 + p3

    first_group = Group('__VIP__', [p0, p1, p2])
    second_group = Group('Special', [p3, p4])
    third_group = first_group + second_group
    print(len(first_group))
    print(second_group)
    print(third_group[0])

    for person in third_group:
         print(person)
