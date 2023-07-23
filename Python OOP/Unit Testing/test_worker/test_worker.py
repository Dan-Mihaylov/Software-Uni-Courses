from worker import Worker

import unittest


class WorkerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Petar", 1200, 1)   # NAME, SALARY, ENERGY

    def test__worker_init__correct_info(self):

        expected_name = "Petar"
        expected_salary = 1200
        expected_energy = 1

        self.assertEqual(expected_name, self.worker.name)
        self.assertEqual(expected_salary, self.worker.salary)
        self.assertEqual(expected_energy, self.worker.energy)

    def test__worker_energy__increment_after_rest(self):

        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test__worker_work_with_0_energy__error_raise(self):

        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        # self.assertIsNotNone(ex)
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test__worker_money__increase_by_salary_when_work(self):

        expected_money = self.worker.money + self.worker.salary

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)

    def test__worker_energy__decrease_by_1_when_work(self):

        self.worker.energy = 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)

    def test__worker_get_info__correct_values(self):

        expected_value = f"Petar has saved 0 money."
        result = self.worker.get_info()

        self.assertEqual(expected_value, result)


if __name__ == "__main__":
    unittest.main()

