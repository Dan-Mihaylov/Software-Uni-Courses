from typing import List


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int):
        self.page = page


class Library:

    def __init__(self):
        self.books: List[Book] = []

    def find_book(self, title: str):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return "Book Not in Library"
