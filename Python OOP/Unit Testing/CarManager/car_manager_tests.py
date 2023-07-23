from car_manager import Car


import unittest


class CarTester(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car("Make", "Model", 1, 5)   # MAKE, MODEL, FUEL CONSUMPTION, FUEL CAPACITY

    def test__init_method__sets_correct_info(self):
        self.assertEqual("Make", self.car.make)
        self.assertEqual("Model", self.car.model)
        self.assertEqual(1, self.car.fuel_consumption)
        self.assertEqual(5, self.car.fuel_capacity)

    def test__make_set_value_to_none__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test__model_set_value_to_none__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test__fuel_consumption_set_value_to_zero_or_smaller__raise_exception(self):

        for value in [0, -1]:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_consumption = value

            self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test__fuel_capacity_set_value_to_zero_or_smaller__raise_exception(self):

        for value in [0, -1]:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_capacity = value

            self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test__fuel_amount_set_value_negative__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test__refuel_set_fuel_to_zero_or_negative__raise_exception(self):

        for value in [0, -1]:
            with self.assertRaises(Exception) as ex:
                self.car.refuel(value)

            self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test__refuel_with_more_than_capacity__capacity_full(self):

        self.car.refuel(10)
        expected_result = self.car.fuel_capacity
        result = self.car.fuel_amount

        self.assertEqual(expected_result, result)

    def test__refuel_with_ok_quantity__add_new_fuel(self):

        self.car.refuel(3)
        self.car.refuel(1)
        expected_result = 4
        result = self.car.fuel_amount

        self.assertEqual(expected_result, result)

    def test__drive_distance__decrease_fuel_amount(self):

        self.car.fuel_amount = 5
        self.car.drive(100)
        self.car.drive(100)

        expected_result = 3
        result = self.car.fuel_amount

        self.assertEqual(expected_result, result)

    def test__drive_distance_with_less_fuel__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
