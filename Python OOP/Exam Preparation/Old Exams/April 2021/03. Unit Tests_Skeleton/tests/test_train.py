from project.train.train import Train
import unittest


class TestTrain(unittest.TestCase):

    def setUp(self) -> None:
        self.train = Train("Name", 10)

    def test__correct_initialization(self):
        self.assertEqual("Name", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test__add__passenger_method_all(self):
        self.train.capacity = 3

        self.train.passengers = ["Person1"]

        result = self.train.add("Person2")
        self.assertEqual(["Person1", "Person2"], self.train.passengers)
        self.assertEqual("Added passenger Person2", result)

        with self.assertRaises(ValueError) as ve:
            self.train.add("Person2")

        self.assertEqual("Passenger Person2 Exists", str(ve.exception))

        self.train.add("Person3")
        self.assertEqual(["Person1", "Person2", "Person3"], self.train.passengers)

        with self.assertRaises(ValueError) as ve:
            self.train.add("Person4")
        self.assertEqual("Train is full", str(ve.exception))

    def test__remove_passenger_method_all_possibilities(self):
        self.train.passengers = ["Person1", "Person2", "Person3"]

        result = self.train.remove("Person1")
        self.assertEqual("Removed Person1", result)

        result = self.train.remove("Person3")
        self.assertEqual("Removed Person3", result)

        with self.assertRaises(ValueError) as ve:
            self.train.remove("Person1")
        self.assertEqual("Passenger Not Found", str(ve.exception))




