from project.pet_shop import PetShop
import unittest


class TestPetShop(unittest.TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop("Name")

    def test__correct_initialization(self):
        self.assertEqual("Name", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test__add_food__all_scenarios(self):
        self.pet_shop.add_food("food1", 10)
        self.assertEqual({"food1": 10}, self.pet_shop.food)

        self.pet_shop.add_food("food1", 10)
        self.assertEqual({"food1": 20}, self.pet_shop.food)

        result = self.pet_shop.add_food("food2", 10)
        self.assertEqual({"food1": 20, "food2": 10}, self.pet_shop.food)
        self.assertEqual("Successfully added 10.00 grams of food2.", result)

        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("food1", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("food1", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test__add_pet__all(self):
        self.pet_shop.add_pet("pet1")
        result = self.pet_shop.add_pet("pet2")

        self.assertEqual(["pet1", "pet2"], self.pet_shop.pets)
        self.assertEqual("Successfully added pet2.", result)

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("pet1")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test__feed_pet__all_cases(self):
        self.pet_shop.food = {"food1": 1000, "food2": 90}
        self.pet_shop.pets = ["pet1", "pet2"]

        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("food1", "pet3")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

        result = self.pet_shop.feed_pet("food4", "pet1")
        self.assertEqual('You do not have food4', result)

        result = self.pet_shop.feed_pet("food2", "pet1")
        self.assertEqual("Adding food...", result)
        self.assertEqual(1090, self.pet_shop.food["food2"])

        result = self.pet_shop.feed_pet("food1", "pet1")
        self.assertEqual("pet1 was successfully fed", result)
        self.assertEqual(900, self.pet_shop.food["food1"])

    def test__repr_method(self):
        expected_zero_animals = f"Shop Name:\n" \
                                f"Pets: "
        expected_with_animas = f"Shop Name:\n" \
                               f"Pets: pet1, pet2, pet3"

        self.assertEqual(expected_zero_animals, self.pet_shop.__repr__())

        self.pet_shop.pets = ["pet1", "pet2", "pet3"]
        self.assertEqual(expected_with_animas, self.pet_shop.__repr__())






if __name__ == "__main__":
    unittest.main()
