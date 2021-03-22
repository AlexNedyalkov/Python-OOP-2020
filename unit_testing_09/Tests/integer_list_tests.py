from unit_testing_09.List.extended_list import IntegerList
import unittest

class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.my_list = IntegerList([])

    def test_init(self):
        int_list = IntegerList('baicho', 'mk', 42)
        self.assertEqual(int_list.get_data(), [42])


    def test_add_element_with_int(self):
        self.assertEqual(self.my_list.add(6), [6])

    def test_add_element_with_non_integer(self):
        # with self.assertRaises(ValueError) as exc:
        #     self.my_list.add(4.5)
        # self.assertEqual(str(exc.exception), 'Element is not Integer')
        self.assertRaises(ValueError, self.my_list.add, 'pesho')

    def test_remove_item_at_correct_index(self):
        self.my_list.add(10)
        el = self.my_list.remove_index(0)
        self.assertEqual(el, 10)

    def test_remove_item_at_incorrect_index(self):
        self.assertRaises(IndexError, self.my_list.remove_index, 2)
        
    def test_get_with_proper_index(self):
        self.my_list.add(19)
        self.assertEqual(self.my_list.get(0), 19)

    def test_get_with_inccorent_index(self):
        self.assertRaises(IndexError, self.my_list.get, 1)

    def test_insert(self):
        self.my_list.add(10)
        self.my_list.insert(0, 19)
        self.assertEqual(self.my_list.get_data(), [19,10])
    
    def test_insert_with_incorrect_index(self):
        with self.assertRaises(IndexError) as exc:
            self.my_list.insert(1, 10)
        self.assertEqual(str(exc.exception), "Index is out of range")

    def test_insert_with_incorrent_value(self):
        self.my_list.add(10)
        with self.assertRaises(ValueError):
            self.my_list.insert(0, 8.5)

    def test_biggest(self):
        self.long_list = IntegerList(1,2,3,100, 5)
        biggest = self.long_list.get_biggest()
        self.assertEqual(100, biggest)

    def test_get_index(self):
        self.my_list.add(19)
        self.assertEqual(0, self.my_list.get_index(19))

if __name__ == '__main__':
    unittest.main()



