from hashtable.hashtable import HashTable
import unittest


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test__key_validator_empty_key__raises(self):
        with self.assertRaises(ValueError) as ve:
            self.table.add("  ", 10)

        self.assertEqual("Key should be a non empty string", str(ve.exception))

    def test__add__adds_items(self):
        self.table.add("Dan", 10)
        self.table.add("Iel", 20)

        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(10, self.table.array[0])
        self.assertEqual(20, self.table.array[1])

    def test__add_existing_key__changes_the_value(self):
        self.table.add("Dan", 10)
        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual(10, self.table.array[0])

        self.table.add("Dan", 20)
        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual(20, self.table.array[0])

        self.table.add("Iel", 20)
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(20, self.table.array[1])

        self.table.add("Iel", 30)
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(30, self.table.array[1])

    def test__add_item_with_assignment_method(self):
        self.table["Dan"] = 10
        self.table["Iel"] = 20

        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(10, self.table.array[0])
        self.assertEqual(20, self.table.array[1])

    def test__add_item_with_assignment_method_change_values_existing_keys(self):
        self.table["Dan"] = 10
        self.table["Iel"] = 20

        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(10, self.table.array[0])
        self.assertEqual(20, self.table.array[1])

        self.table["Dan"] = 30
        self.table["Iel"] = 40

        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual("Iel", self.table.keys[1])
        self.assertEqual(30, self.table.array[0])
        self.assertEqual(40, self.table.array[1])

    def test__if_you_need_to_double_array_when_not_full__returns_false(self):
        self.table.add("Dan", 10)
        self.assertFalse(self.table._check_if_you_need_to_double_array())

    def test__if_you_need_to_double_array_when_full__returns_true(self):
        self.table.keys = ["Dan", "Iel", "Pet", "Er"]
        self.table.array = [10, 11, 12, 13, 14]

        self.assertTrue(self.table._check_if_you_need_to_double_array())

    def test__doubles_correctly__array_size_increases(self):
        self.assertEqual(4, len(self.table))
        for index in range(5):
            self.table.add(f"{index}", index)

        self.assertEqual(8, len(self.table))

        for index in range(6, 10):
            self.table.add(f"{index}", index)

        self.assertEqual(16, len(self.table))

    def test__get_item_by_assignment__returns_item(self):
        self.table.add("Dan", 10)

        result = self.table["Dan"]
        self.assertEqual(10, result)

    def test__remove_non_existent__raises(self):

        with self.assertRaises(KeyError) as ke:
            self.table.remove("Dan")
        self.assertEqual("'Dan not in HashTable'", str(ke.exception))

    def test__remove__removes_key_value_pair(self):

        self.table.add("Dan", 10)
        self.table.add("Jon", 20)

        self.table.remove("Jon")
        self.assertEqual("Dan", self.table.keys[0])
        self.assertEqual("", self.table.keys[1])

        self.assertEqual(10, self.table.array[0])
        self.assertEqual(None, self.table.array[1])

