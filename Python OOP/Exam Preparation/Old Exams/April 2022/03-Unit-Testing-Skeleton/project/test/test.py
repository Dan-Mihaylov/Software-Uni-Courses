from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTester(unittest.TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Name", 18, 100)
        """
        self.name = "Name"
        self.age = 18
        self.points = 100
        self.wins = []
        """

    def test__init__correct_info(self):
        self.assertEqual("Name", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test__set_name_correct_value__change_name(self):

        self.player.name = "Test"
        expected_result = "Test"
        actual_result = self.player.name

        self.assertEqual(expected_result, actual_result)

    def test__set_name_wrong_values__raise_value_error(self):

        for name in ["No", "N"]:
            with self.assertRaises(ValueError) as ve:
                self.player.name = name

            self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test__set_age_correct_value__change_age(self):

        self.player.age = 20
        expected_result = 20
        actual_result = self.player.age

        self.assertEqual(expected_result, actual_result)

    def test__set_age_wrong_values__raise_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test__add_win_new_win__adds_win_to_list(self):

        self.player.add_new_win("Tournament Name")
        expected_result = ["Tournament Name"]
        actual_result = self.player.wins

        self.assertEqual(expected_result, actual_result)

        self.player.add_new_win("New Win")

        expected_result = ["Tournament Name", "New Win"]
        actual_result = self.player.wins

        self.assertEqual(expected_result, actual_result)

    def test__add_win_same_tournament__returns_correct_message(self):

        self.player.wins = ["Tournament Name"]
        expected_result = "Tournament Name has been already added to the list of wins!"
        actual_result = self.player.add_new_win("Tournament Name")

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(["Tournament Name"], self.player.wins)

    def test__less_than_other_player_better__return_correct_message(self):

        other_player = TennisPlayer("OtherName", 20, 101)

        expected_result = "OtherName is a top seeded player and he/she is better than Name"
        actual_result = self.player < other_player

        self.assertEqual(expected_result, actual_result)

    def test__less_than_other_player_worst__return_correct_message(self):

        other_player = TennisPlayer("OtherName", 20, 99)

        expected_result = "Name is a better player than OtherName"
        actual_result = self.player < other_player

        self.assertEqual(expected_result, actual_result)

    def test__string_representation_no_wins__returns_correct_string(self):

        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"
        actual_result = self.player.__str__()

        self.assertEqual(expected_result, actual_result)

    def test__string_rep_one_win__returns_correct_string(self):

        self.player.wins = ["Win 1"]

        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: Win 1"
        actual_result = self.player.__str__()

        self.assertEqual(expected_result, actual_result)

    def test_string_rep_two_wins__returns_correct_format_string(self):

        self.player.wins = ["Win 1", "Win 2"]

        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: Win 1, Win 2"
        actual_result = self.player.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()

