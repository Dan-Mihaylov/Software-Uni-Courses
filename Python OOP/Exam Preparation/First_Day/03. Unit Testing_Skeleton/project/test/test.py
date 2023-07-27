from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Name", 2000, 10.0)

        """
        self.name = "Name"
        self.year = 2000
        self.rating = 10.0
        self.actors = []
        """

    def test__correct_initializing(self):
        self.assertEqual("Name", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(10.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__name_set_correct__return_new_name_or_raise(self):
        self.movie.name = "New Name"
        self.assertEqual("New Name", self.movie.name)

        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test__year_set_correct__return_new_year_or_raise(self):

        self.movie.year = 1900
        self.assertEqual(1900, self.movie.year)

        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test__add_actor_new_name__add_name_to_list(self):
        self.movie.add_actor("Name")
        self.assertListEqual(["Name"], self.movie.actors)

        self.movie.add_actor("Pepe")
        self.assertListEqual(["Name", "Pepe"], self.movie.actors)

    def test_add_actor_name_already_in_list__does_not_add_name_again(self):
        self.movie.actors = ["Name"]
        result = self.movie.add_actor("Name")

        self.assertListEqual(["Name"], self.movie.actors)
        self.assertEqual("Name is already added in the list of actors!", result)

    def test__greater_than_first_and_second_movie_better__returns_correct_string(self):

        other_movie = Movie("Other", 2000, 9)

        expected_result = f'"Name" is better than "Other"'
        actual_result = self.movie.__gt__(other_movie)
        self.assertEqual(expected_result, actual_result)

        other_movie.rating = 11
        expected_result = f'"Other" is better than "Name"'
        actual_result = self.movie.__gt__(other_movie)
        self.assertEqual(expected_result, actual_result)

        other_movie.rating = 10
        actual_result = self.movie.__gt__(other_movie)
        self.assertEqual(expected_result, actual_result)

    def test__string_representation_represents_correctly(self):
        expected_result = f"Name: Name\n" \
                          f"Year of Release: 2000\n"\
                          f"Rating: 10.00\n"\
                          f"Cast: "
        actual_result = self.movie.__repr__()
        self.assertEqual(expected_result, actual_result)

        self.movie.actors = ["Actor_One", "Actor_Two"]
        expected_result = f"Name: Name\n" \
                          f"Year of Release: 2000\n" \
                          f"Rating: 10.00\n" \
                          f"Cast: Actor_One, Actor_Two"
        actual_result = self.movie.__repr__()
        self.assertEqual(expected_result, actual_result)
