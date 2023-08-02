from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(10)

    def test__correct_initialization(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test__books_limit_incorrect_value__raises(self):

        for value in range(-1, 1):
            with self.assertRaises(ValueError) as ve:
                self.store.books_limit = value
            self.assertEqual(f"Books limit of {value} is not valid", str(ve.exception))

    def test__dunder_len__returns_all_books_in_store(self):

        self.assertEqual(0, len(self.store))

        self.store.availability_in_store_by_book_titles = {
            "book1": 3,
            "book2": 2,
            "book3": 1
        }

        result = self.store.__len__()
        self.assertEqual(6, result)

    def test__receive_book_no_capacity_left__raises(self):

        self.store.availability_in_store_by_book_titles = {"book1": 9, "book2": 1}

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("book1", 2)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({"book1": 9, "book2": 1}, self.store.availability_in_store_by_book_titles)

    def test__receive_book_correct_info__adds_book_returns_message(self):

        self.store.receive_book("book1", 3)
        self.assertEqual({"book1": 3}, self.store.availability_in_store_by_book_titles)

        self.store.receive_book("book1", 3)
        self.assertEqual({"book1": 6}, self.store.availability_in_store_by_book_titles)

        self.store.receive_book("book2", 2)
        expected = {"book1": 6, "book2": 2}
        self.assertEqual(expected, self.store.availability_in_store_by_book_titles)
        result = self.store.receive_book("book2", 2)
        self.assertEqual({"book1": 6, "book2": 4}, self.store.availability_in_store_by_book_titles)

        self.assertEqual("4 copies of book2 are available in the bookstore.", result)

    def test__sell_book_title_not_there_and_sell_more_than_have__raises(self):

        self.store.availability_in_store_by_book_titles = {"book1": 3}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book2", 2)

        self.assertEqual("Book book2 doesn't exist!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book1", 4)

        expected = "book1 has not enough copies to sell. Left: 3"
        self.assertEqual(expected, str(ex.exception))

    def test__sell_book_enough_books__books_decrease_return_message(self):

        self.store.availability_in_store_by_book_titles = {"book1": 4, "book2": 2}

        self.store.sell_book("book1", 2)
        self.assertEqual({"book1": 2, "book2": 2}, self.store.availability_in_store_by_book_titles)

        self.store.sell_book("book1", 1)
        self.assertEqual({"book1": 1, "book2": 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, self.store.total_sold_books)

        result = self.store.sell_book("book2", 1)
        self.assertEqual({"book1": 1, "book2": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(4, self.store.total_sold_books)
        self.assertEqual("Sold 1 copies of book2", result)

    def test__str_method__returns_correct_format(self):

        self.store.availability_in_store_by_book_titles = {"book1": 3, "book2": 2, "book3": 5}
        self.store.sell_book("book1", 2)    # 1
        self.store.sell_book("book2", 1)    # 1
        self.store.sell_book("book3", 2)    # 3

        expected = "Total sold books: 5\n" \
            "Current availability: 5\n" \
            " - book1: 1 copies\n" \
            " - book2: 1 copies\n" \
            " - book3: 3 copies"
        result = self.store.__str__()

        self.assertEqual(expected, result)

        self.store.sell_book("book1", 1)
        self.store.sell_book("book2", 1)
        self.store.sell_book("book3", 3)

        expected = "Total sold books: 10\n" \
                   "Current availability: 0\n" \
                   " - book1: 0 copies\n" \
                   " - book2: 0 copies\n" \
                   " - book3: 0 copies"

        result = self.store.__str__()

        self.assertEqual(expected, result)

        self.new_store = Bookstore(10)
        expected = "Total sold books: 0\n" \
                   "Current availability: 0"
        result = self.new_store.__str__()
        self.assertEqual(expected, result)



