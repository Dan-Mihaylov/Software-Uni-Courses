from extended_list import IntegerList


import unittest


class IntegerListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, 4, 5)

    def test__init_taking_only_integers__doesnt_add_other(self):

        integer_list = IntegerList(1, 2, 3, 3.5, "hello", True)

        self.assertListEqual([1, 2, 3], integer_list.get_data())

    def test__add_operation_adding_element__returning_the_list(self):

        expected_result = [1, 2, 3, 4, 5, 6]
        self.integer_list.add(6)

        self.assertListEqual(expected_result, self.integer_list.get_data())

    def test__add_operation_adding_non_integer_element__raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(6.5)

        self.assertIsNotNone(ve)

    def test__remove_index_element__removes_element_and_returns_it(self):

        expected_result_a = 1
        a = self.integer_list.remove_index(0)

        expected_list_result = [2, 3, 4, 5]

        self.assertEqual(expected_result_a, a)
        self.assertListEqual(expected_list_result, self.integer_list.get_data())

    def test__remove_index_element_over_list_length__raises_index_error(self):

        index = len(self.integer_list.get_data())

        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(index)

        self.assertIsNotNone(ie)

    def test__get_element__returns_element(self):

        index = 0
        expected_element = 1
        result = self.integer_list.get(index)

        self.assertEqual(expected_element, result)

    def test__get_element__element_over_range(self):

        index = len(self.integer_list.get_data())

        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(index)

        self.assertIsNotNone(ie)

    def test__insert_el_on_index__inserts_el(self):

        index = 0
        element = 6

        expected_result = [6, 1, 2, 3, 4, 5]
        self.integer_list.insert(index, element)
        result = self.integer_list.get_data()

        self.assertListEqual(expected_result, result)

    def test__insert_el_on_index_index_over_range__raises_index_error(self):

        index = len(self.integer_list.get_data())
        value = 6

        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(index, value)

        self.assertIsNotNone(ie)

    def test__insert_el_on_index_element_wrong_type__raises_value_error(self):

        index = 0
        values = [6.5, True, "No"]

        for value in values:
            with self.assertRaises(ValueError) as ve:
                self.integer_list.insert(index, value)

            self.assertIsNotNone(ve)

    def test__get_biggest_el__returns_the_max_value_int(self):

        expected_result = 5
        result = self.integer_list.get_biggest()

        self.assertEqual(expected_result, result)

    def test__get_index_el__returns_the_index_of_the_element(self):

        expected_result = 1
        result = self.integer_list.get_index(2)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()

