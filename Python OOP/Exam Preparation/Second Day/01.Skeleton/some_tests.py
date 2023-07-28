# from project.movie_app import MovieApp
# from project.movie_specification.fantasy import Fantasy
# from project.movie_specification.thriller import Thriller
# from project.movie_specification.action import Action
# from project.user import User
# import unittest
#
#
# class TestMovieApp(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.daniel = User("Daniel", 20)
#         self.peter = User("Peter", 20)
#         self.lilly = User("Lilly", 20)
#         self.fantasy = Fantasy("Interstellar", 2013, self.peter, 16)
#         self.thriller = Thriller("Jango Unchained", 2015, self.peter, 16)
#         self.action = Action("Fast 10", 2023, self.daniel, 13)
#         self.movie_app = MovieApp()
#
#     def test__likes_like_a_movie_see_what_happens(self):
#
#         self.movie_app.movies_collection = [self.fantasy, self.thriller, self.action]
#         self.movie_app.users_collection = [self.daniel, self.peter, self.lilly]
#
#         self.movie_app.like_movie("Daniel", self.fantasy)
#         self.assertEqual(1, self.fantasy.likes)
#         self.assertListEqual([self.fantasy], self.daniel.movies_liked)
#         self.movie_app.like_movie("Lilly", self.fantasy)
#         self.assertEqual(2, self.fantasy.likes)
#         self.movie_app.like_movie("Daniel", self.thriller)
#         self.assertListEqual([self.fantasy, self.thriller], self.daniel.movies_liked)
#
#         # dislike the movie now
#
#         self.movie_app.dislike_movie("Daniel", self.fantasy)
#         self.movie_app.dislike_movie("Lilly", self.fantasy)
#         self.assertEqual(0, self.fantasy.likes)
#         self.assertListEqual([self.thriller], self.daniel.movies_liked)
#         self.movie_app.dislike_movie("Daniel", self.thriller)
#         self.assertListEqual([], self.daniel.movies_liked)
#
#         # Owner likes movie
#
#         with self.assertRaises(Exception) as ex:
#             self.movie_app.like_movie("Peter", self.fantasy)
#         self.assertEqual("Peter is the owner of the movie Interstellar!", str(ex.exception))
#
#         # same person likes movie again
#
#         with self.assertRaises(Exception) as ex:
#             self.movie_app.like_movie("Daniel", self.fantasy)
#             self.movie_app.like_movie("Daniel", self.fantasy)
#         self.assertEqual("Daniel already liked the movie Interstellar!", str(ex.exception))
#
#         # dislike movie that you haven't liked
#
#         with self.assertRaises(Exception) as ex:
#             self.daniel.movies_liked = []
#             self.movie_app.dislike_movie("Daniel", self.fantasy)
#         self.assertEqual("Daniel has not liked the movie Interstellar!", str(ex.exception))
#
#
#
