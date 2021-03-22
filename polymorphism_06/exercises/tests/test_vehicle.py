from polymorphism_06.exercises.vehicle_01 import Car, Truck, Vehicle
import unittest

class TestCar(unittest.TestCase):

    def setUp(self):
        self.my_car = Car(100, 10)
    # def test_abstract_class(self):
    #     with self.assertRaises(expected_exception=Exception) as exc:
    #         self.vehicle = Vehicle()

    def test_init_car(self):
        self.assertEqual(self.my_car.fuel_quantity, 100)
        self.assertEqual(self.my_car.fuel_consumption, 10)
        self.assertEqual(self.my_car.fuel_consumption_increase, 0.9)

    def test_drive_car_with_enough_fuel(self):
        self.my_car.drive(1)
        self.assertEqual(self.my_car.fuel_quantity, 89.1)

    def test_drive_car_with_not_enough_fuel(self):
        self.my_car.drive(10)
        self.assertEqual(self.my_car.fuel_quantity, 100)

    def test_car_refuel(self):
        self.my_car.refuel(10)
        self.assertEqual(self.my_car.fuel_quantity, 110)

class TestTruck(unittest.TestCase):

    def setUp(self):
        self.my_truck = Truck(120, 20)

    def test_init_truck(self):
        self.assertEqual(self.my_truck.fuel_quantity, 120)
        self.assertEqual(self.my_truck.fuel_consumption, 20)
        self.assertEqual(self.my_truck.fuel_consumption_increase, 1.6)
        self.assertEqual(self.my_truck.hole_refuel_damage, 0.05)

    def test_drive_truck_with_not_enough_fuel(self):
        self.my_truck.drive(10)
        self.assertEqual(self.my_truck.fuel_quantity, 120)

    def test_truck_refuel(self):
        self.my_truck.refuel(100)
        self.assertEqual(self.my_truck.fuel_quantity, 215)

    def test_drive_truck_with_enough_fuel(self):
        self.my_truck.drive(1)
        self.assertEqual(self.my_truck.fuel_quantity, 98.4)

if __name__ == '__main__':
    unittest.main()