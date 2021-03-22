from unit_testing_09.CarManager.car_manager import Car
import unittest

class CarTests(unittest.TestCase):

    def setUp(self):
        self.my_car = Car(make = 'WV', model = 'Golf', fuel_consumption = 10, fuel_capacity=100)

    def test_init(self):
        self.assertEqual('WV', self.my_car.make)
        self.assertEqual('Golf', self.my_car.model)
        self.assertEqual(10, self.my_car.fuel_consumption)
        self.assertEqual(100, self.my_car.fuel_capacity)


    def test_init_with_empty_make(self):
          with self.assertRaises(Exception) as exc:
               self.my_car.make = ''
          self.assertEqual(str(exc.exception), "Make cannot be null or empty!")

    def test_init_with_empty_model(self):
          with self.assertRaises(Exception) as exc:
               self.my_car.model = ''

    def test_raising_error_when_negative_capacity(self):
        with self.assertRaises(Exception) as exc:
            self.negative_capacity_car = Car(make = 'WV', model = 'Golf', fuel_consumption = 10, fuel_capacity = -100)
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_raising_error_when_negative_consumption(self):
        with self.assertRaises(Exception) as exc:
            self.negative_consumption_car = Car(make = 'WV', model = 'Golf', fuel_consumption = -10, fuel_capacity = 100)
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")


    def test_raise_negative_fuel_amount(self):
        with self.assertRaises(expected_exception = Exception) as exc:
            self.my_car.fuel_amount = -10
        self.assertEqual(str(exc.exception), 'Fuel amount cannot be negative!')

    def test_refuel_with_proper_fuel_amount(self):
        self.my_car.refuel(20)
        self.assertEqual(self.my_car.fuel_amount, 20)

    def test_refuel_with_negative_fuel(self):
        self.assertRaises(Exception, self.my_car.refuel, -10)

    def test_refuel_with_higher_than_capacity_amount(self):
        self.my_car.refuel(110)
        self.assertEqual(self.my_car.fuel_amount, 100)

    def test_drive_with_big_distance(self):
        self.assertRaises(Exception, self.my_car.drive, 100)

    def test_drive_with_small_distance(self):
        self.my_car.refuel(50)
        self.my_car.drive(100)
        self.assertEqual(self.my_car.fuel_amount, 40)

if __name__ == '__main__':
    unittest.main()
