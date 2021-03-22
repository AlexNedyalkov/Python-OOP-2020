from unit_testing_09.test_worker.worker import Worker
from parameterized import parameterized
import unittest

class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Pesho", 110, 10)

    def test_correct_name_salary_energy(self):
        self.assertEqual(self.worker.name, "Pesho")
        self.assertEqual(self.worker.salary, 5)
        self.assertEqual(self.worker.energy, 10)

    def test_incremental_energy(self):
        first_worker_energy = self.worker.energy
        self.worker.rest()
        new_worker_energy = self.worker.energy
        self.assertEqual(first_worker_energy + 1, new_worker_energy)

    @parameterized.expand([
        (-42,),
        (-10,),
        (-5,),
    ])
    def test_working_with_negative_energy(self, energy):
        self.worker.energy = energy
        with self.assertRaises(Exception):
            self.worker.work()

    def test_working_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_increase_salary(self):
        first_worker_money = self.worker.money
        self.worker.work()
        new_worker_money = self.worker.money
        self.assertEqual(first_worker_money + self.worker.salary , new_worker_money)

    def test_energy_decreases_after_working(self):
        first_energy = self.worker.energy
        self.worker.work()
        new_energy = self.worker.energy
        self.assertEqual(first_energy - 1, new_energy)
        
    def test_get_info(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())

if __name__ == '__main__':
    unittest.main()