from ..groups_02 import Person, Group
import unittest

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person("Pesho", "Baichev")

    def test_init_person(self):
        self.assertEqual((self.person.name, self.person.surname), ('Pesho', 'Baichev'))

    def test_str_method_person(self):
        self.assertEqual(str(self.person), 'Pesho Baichev')

    def test_add_method_person(self):
        other_person = Person('Ivan', 'Ivanov')
        added_person = self.person + other_person 
        self.assertEqual((added_person.name, added_person.surname), ('Pesho', 'Ivanov'))
        self.assertEqual(str(added_person), 'Pesho Ivanov')

class TestGroup(unittest.TestCase):

    def setUp(self):
        self.person = Person("Pesho", "Baichev")
        self.other_person = Person('Baicho', 'Peshev')
        self.group = Group('Baba', [self.person, self.other_person])

    def test_init_group(self):
         self.assertEqual(self.group.name, 'Baba')
         self.assertEqual(self.group.people, [self.person, self.other_person])

    def test_len_of_group(self):
        self.assertEqual(len(self.group), 2)

    def test_str_of_group(self):
        self.assertEqual(str(self.group), 'Group Baba with member Pesho Baichev, Baicho Peshev')

    def test_get_item_group(self):
        self.assertEqual(str(self.group[0]), 'Person 0: Pesho Baichev')
        self.assertEqual(str(self.group[1]), 'Person 1: Baicho Peshev')

    def test_add_other_group(self):
        p3 = Person('Ivan', 'Ivanov')
        p4 = Person('Gosho', 'Goshev')
        new_group = Group('mama', [p3, p4])
        added_group = self.group + new_group
        self.assertEqual(added_group.name, 'Babamama')
        self.assertEqual(added_group.people, [self.person, self.other_person, p3, p4])
        self.assertEqual(len(added_group), 4)
        self.assertEqual(str(added_group), 'Group Babamama with member Pesho Baichev, Baicho Peshev, Ivan Ivanov, Gosho Goshev')
        
if __name__ == '__main__':
    unittest.main()