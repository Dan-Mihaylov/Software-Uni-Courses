from cat import Cat


import unittest


class TestCat(unittest.TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Catuchino")

    def test__cat_size__increase_after_eating(self):

        expected_size = self.cat.size + 1
        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)

    def test__cat_fed_after_eating__expect_true(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test__cat_eat_after_already_fed__raise_error(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertIsNotNone(ex)
        #self.assertEqual("Already fed.", str(ex.exception))

    def test__cat_cannot_sleep_if_not_fed__raise_error(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)
        # self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test__cat_not_sleepy_after_sleeping__false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
