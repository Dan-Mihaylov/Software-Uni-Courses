from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(5)
        """
        self.size = 5
        self.plants = {}
        self.workers = []
        """

    def test__initialization_correct(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test__size_setter__sets_correct_value_or_raises(self):
        self.plantation.size = 10
        self.assertEqual(10, self.plantation.size)

        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test__hire_worker__adds_worker_to_workers_or_raises_if_already_hired(self):
        result = self.plantation.hire_worker("Peter")
        self.assertListEqual(["Peter"], self.plantation.workers)
        self.assertEqual("Peter successfully hired.", result)

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Peter")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test__len_returns_count_of_plants_planted(self):
        result = self.plantation.__len__()
        self.assertEqual(0, result)

        self.plantation.plants = {
            "Peter": ["Plant1", "Plant2"],
            "Daniel": ["Plant1"]
        }
        result = self.plantation.__len__()
        self.assertEqual(3, result)

    def test__planting_worker_not_in_workers__raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Daniel", "Plant1")
        self.assertEqual("Worker with name Daniel is not hired!", str(ve.exception))

    def test__planting_len_bigger_equal_than_size__raises(self):
        self.plantation.size = 1
        self.plantation.workers = ["Daniel"]
        self.plantation.plants = {"Daniel": ["Plant1"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Daniel", "Plant2")
        self.assertEqual("The plantation is full!", str(ve.exception))

        self.plantation.plants = {"Daniel": ["Plant1", "Plant2"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Daniel", "Plant3")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test__planting_worker_not_in_plants_keys__adds_worker_and_plant(self):
        self.plantation.workers = ["Daniel"]
        result = self.plantation.planting("Daniel", "Plant1")

        self.assertEqual({"Daniel": ["Plant1"]}, self.plantation.plants)
        self.assertEqual("Daniel planted it's first Plant1.", result)

    def test__planting_worker_in_plants_keys__add_plant_to_worker(self):
        self.plantation.workers = ["Daniel"]
        self.plantation.plants = {"Daniel": ["Plant1"]}

        result = self.plantation.planting("Daniel", "Plant2")
        self.assertEqual({"Daniel": ["Plant1", "Plant2"]}, self.plantation.plants)
        self.assertEqual("Daniel planted Plant2.", result)

    def test__str_returns_correct(self):
        # print with no workers
        expected = "Plantation size: 5\n"
        self.assertEqual(expected, self.plantation.__str__())

        # print with one worker
        self.plantation.workers = ["Daniel"]
        expected = "Plantation size: 5\nDaniel"
        self.assertEqual(expected, self.plantation.__str__())

        # print more workers
        self.plantation.workers = ["Daniel", "Peter"]
        expected = "Plantation size: 5\nDaniel, Peter"
        self.assertEqual(expected, self.plantation.__str__())

        # print names and plants
        self.plantation.plants = {"Daniel": ["Plant1"], "Peter": ["Plant1", "Plant2"]}
        expected = "Plantation size: 5\n" \
                   "Daniel, Peter\n" \
                   "Daniel planted: Plant1\n" \
                   "Peter planted: Plant1, Plant2"
        self.assertEqual(expected, self.plantation.__str__())

    def test__repr_returns_correct(self):
        expected = "Size: 5\n" \
                   "Workers: "
        self.assertEqual(expected, self.plantation.__repr__())

        self.plantation.workers = ["Daniel"]
        expected = "Size: 5\n" \
                   "Workers: Daniel"
        self.assertEqual(expected, self.plantation.__repr__())

        self.plantation.workers = ["Daniel", "Peter"]
        expected = "Size: 5\n" \
                   "Workers: Daniel, Peter"
        self.assertEqual(expected, self.plantation.__repr__())

