from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
        self.PRICE_INCREMENT = 1.5

        self.military_robot = Robot("Robot1", "Military", 10, 10.00)
        self.education_robot = Robot("Robot2", "Education", 10, 10.00)

    def test_correct_initialization(self):
        self.assertEqual("Robot1", self.military_robot.robot_id)
        self.assertEqual("Military", self.military_robot.category)
        self.assertEqual(10, self.military_robot.available_capacity)
        self.assertEqual(10.00, self.military_robot.price)
        self.assertEqual([], self.military_robot.hardware_upgrades)
        self.assertEqual([], self.military_robot.software_updates)

    def test__category_correct_category_given__creates_instance(self):
        for category in self.ALLOWED_CATEGORIES:
            self.military_robot.category = category
            self.assertEqual(category, self.military_robot.category)

    def test__category_wrong_category_given__raises(self):
        with self.assertRaises(ValueError) as ve:
            self.military_robot.category = "New Category"
        expected_result = f"Category should be one of '{self.ALLOWED_CATEGORIES}'"
        self.assertEqual(expected_result, str(ve.exception))

    def test__price_correct_value__changes_price(self):
        self.military_robot.price = 20.00
        self.assertEqual(20.00, self.military_robot.price)

    def test__price_negative_value__raises(self):

        with self.assertRaises(ValueError) as ve:
            self.military_robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test__upgrade_data_correct__adds_upgrade_to_list_increases_price(self):
        result = self.military_robot.upgrade("Drive", 10.00)
        self.assertEqual(25.00, self.military_robot.price)
        self.assertEqual(["Drive"], self.military_robot.hardware_upgrades)
        expected = 'Robot Robot1 was upgraded with Drive.'
        self.assertEqual(expected, result)

        result = self.military_robot.upgrade("SSD", 10.00)
        expected = 'Robot Robot1 was upgraded with SSD.'
        self.assertEqual(40.00, self.military_robot.price)
        self.assertEqual(["Drive", "SSD"], self.military_robot.hardware_upgrades)
        self.assertEqual(expected, result)

    def test__upgrade_component_present__returns_message(self):
        self.military_robot.hardware_upgrades = ["Drive"]
        result = self.military_robot.upgrade("Drive", 10.00)
        self.assertEqual("Robot Robot1 was not upgraded.", result)
        self.assertEqual(10.00, self.military_robot.price)
        self.assertEqual(["Drive"], self.military_robot.hardware_upgrades)

    def test__update_wrong_info_all_cases__raises(self):
        self.military_robot.software_updates = [1.0, 1.1]

        for version in [0.0, 1.1]:
            result = self.military_robot.update(version, 5)
            self.assertEqual("Robot Robot1 was not updated.", result)
        self.assertEqual([1.0, 1.1], self.military_robot.software_updates)
        self.assertEqual(10, self.military_robot.available_capacity)

        result = self.military_robot.update(2.0, 20)
        self.assertEqual("Robot Robot1 was not updated.", result)
        self.assertEqual([1.0, 1.1], self.military_robot.software_updates)
        self.assertEqual(10, self.military_robot.available_capacity)

    def test__update_correct_info__adds_update_returns_message(self):

        self.military_robot.software_updates = [1.0, 2.0]

        self.military_robot.update(3.0, 3)
        self.assertEqual([1.0, 2.0, 3.0], self.military_robot.software_updates)
        self.assertEqual(7, self.military_robot.available_capacity)

        result = self.military_robot.update(4.0, 2)
        expected = 'Robot Robot1 was updated to version 4.0.'
        self.assertEqual([1.0, 2.0, 3.0, 4.0], self.military_robot.software_updates)
        self.assertEqual(5, self.military_robot.available_capacity)
        self.assertEqual(expected, result)

    def test__gt_dunder__returns_correct_message(self):
        result = self.military_robot.__gt__(self.education_robot)
        expected = 'Robot with ID Robot1 costs equal to Robot with ID Robot2.'
        self.assertEqual(expected, result)

        # self price bigger
        self.military_robot.price = 20.00

        result = self.military_robot.__gt__(self.education_robot)
        expected = 'Robot with ID Robot1 is more expensive than Robot with ID Robot2.'
        self.assertEqual(expected, result)

        # other price bigger
        self.education_robot.price = 50.00

        result = self.military_robot.__gt__(self.education_robot)
        expected = 'Robot with ID Robot1 is cheaper than Robot with ID Robot2.'
        self.assertEqual(expected, result)
