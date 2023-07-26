from project.mammal import Mammal


import unittest


class MammalTester(unittest.TestCase):

    def setUp(self) -> None:
        self.animal = Mammal("Name", "Type", "Sound")

    def test__make_sound__return_correct_info(self):

        expected_result = "Name makes Sound"
        result = self.animal.make_sound()

        self.assertEqual(expected_result, result)

    def test__get_kingdom__returns_animals(self):

        expected_result = "animals"
        result = self.animal.get_kingdom()

        self.assertEqual(expected_result, result)

    def test__info__returns__correct_info(self):

        expected_result = "Name is of type Type"
        result = self.animal.info()

        self.assertEqual(expected_result, result)
