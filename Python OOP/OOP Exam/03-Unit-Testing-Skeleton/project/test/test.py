from project.second_hand_car import SecondHandCar
import unittest


class TestSecondHandCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car_one = SecondHandCar("model1", "type1", 10_000, 5000.00)
        self.car_two = SecondHandCar("model2", "type1", 20_000, 10_000.00)

    def test__correct_initialization(self):
        self.assertEqual("model1", self.car_one.model)
        self.assertEqual("type1", self.car_one.car_type)
        self.assertEqual(10000, self.car_one.mileage)
        self.assertEqual(5000.00, self.car_one.price)
        self.assertEqual([], self.car_one.repairs)

    def test__price_incorrect__raises(self):

        with self.assertRaises(ValueError) as ve:
            car = SecondHandCar("Model2", "Type", 10000, 1.0)
        self.assertEqual(f'Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            car = SecondHandCar("Model2", "Type", 10000, 0)
        self.assertEqual(f'Price should be greater than 1.0!', str(ve.exception))

    def test__mileage__incorrect_raises(self):

        with self.assertRaises(ValueError) as ve:
            car = SecondHandCar("Model2", "Type", 100, 1000)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            car = SecondHandCar("Model2", "Type", 90, 1000)
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test__set_promotional_price_all_scenarios(self):

        with self.assertRaises(ValueError) as ve:
            self.car_one.set_promotional_price(5000.00)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car_one.set_promotional_price(10000.00)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        result = self.car_one.set_promotional_price(4000.00)
        self.assertEqual(4000.00, self.car_one.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test__need_repair_all_scenarios(self):

        result = self.car_one.need_repair(2501.00, "repair1")
        self.assertEqual('Repair is impossible!', result)

        self.car_one.need_repair(2500.00, "repair1")
        result = self.car_one.need_repair(500.00, "repair2")

        self.assertEqual(["repair1", "repair2"], self.car_one.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(8000.00, self.car_one.price)

    def test__dunder__gt(self):
        car_type_wrong = SecondHandCar("Model", "TYPE", 10000, 10000)
        result = self.car_one > car_type_wrong
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

        result = self.car_one > self.car_two
        self.assertFalse(result)

        result = self.car_two > self.car_one
        self.assertTrue(result)

    def test__str_method(self):

        expected_res = f"""Model model1 | Type type1 | Milage 10000km\nCurrent price: 5000.00 | Number of Repairs: 0"""
        self.assertEqual(expected_res, str(self.car_one))

        expected_res = f"""Model model1 | Type type1 | Milage 10000km\nCurrent price: 5000.00 | Number of Repairs: 3"""

        self.car_one.repairs = ["repair1", "repair2", "repair3"]
        self.assertEqual(expected_res, str(self.car_one))

