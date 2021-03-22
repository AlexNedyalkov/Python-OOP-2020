from .cat import Cat
from parameterized import parameterized
import unittest



class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat('Pesho')

    def test_init(self):
        self.assertEqual(self.cat.name, 'Pesho')

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(str(exc.exception), 'Already fed.')

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()