from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self):
        pass


class FormatByContent(Formatter):
    def format(self, obj):
        if obj.content:
            return obj.content
        else:
            return f"{obj} not the right type"


class Printer():

    def __init__(self, obj, formatter: Formatter):
        self.obj = obj
        self.formatter = formatter

    def print_book(self):
        formatter = self.formatter
        return formatter.format(self.obj)
