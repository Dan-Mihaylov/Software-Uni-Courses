from project.vehicle import Vehicle
import unittest


class VehicleTester(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(10.0, 100.0)
        """
        self.fuel = 10.0
        self.capacity = 10.0
        self.horse_power = 100.0
        self.fuel_consumption = 1.25
        """

    def test__init__all_values_correct(self):
        self.assertEqual(10.0, self.vehicle.fuel)
        self.assertEqual(100.0, self.vehicle.horse_power)
        self.assertEqual(10.0, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test__drive_distance_enough_fuel__decrease_fuel(self):

        self.vehicle.drive(2)
        self.vehicle.drive(2)

        expected_fuel = 5.0
        result_fuel = self.vehicle.fuel

        self.assertEqual(expected_fuel, result_fuel)

    def test__drive_distance_not_enough_fuel__raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(2)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test__refuel_with_correct_fuel__increase_fuel(self):

        self.vehicle.fuel = 0
        self.vehicle.refuel(5.0)
        self.vehicle.refuel(5.0)

        expected_fuel = 10.0
        result_fuel = self.vehicle.fuel

        self.assertEqual(expected_fuel, result_fuel)

    def test__refuel_with_wrong_fuel_amount__raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2.0)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test__str_representation__return_correct_string(self):

        expected_result = "The vehicle has 100.0 horse power with 10.0 fuel left and 1.25 fuel consumption"
        actual_result = self.vehicle.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
