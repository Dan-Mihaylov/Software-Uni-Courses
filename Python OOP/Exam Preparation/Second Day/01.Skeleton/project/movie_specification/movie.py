from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):
    AGE_RESTRICTIONS = {
        "Fantasy": 6,
        "Action": 12,
        "Thriller": 16
    }

    def __init__(self, title: str, year: int, owner: User, age_restriction: int = None):
        self.title = title
        self.year = year
        self.owner = owner
        self.likes = 0
        self.age_restriction = age_restriction

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):

        if value is None:
            self.__age_restriction = self.AGE_RESTRICTIONS[self.__class__.__name__]

        elif value < self.AGE_RESTRICTIONS[self.__class__.__name__]:
            raise ValueError(f"{self.__class__.__name__} movies must be restricted for audience under"
                             f" {self.AGE_RESTRICTIONS[self.__class__.__name__]} years!")

        else:
            self.__age_restriction = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):

        if len(value) == 0:
            raise ValueError("The title cannot be empty string!")

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):

        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")

        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):

        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")

        self.__owner = value

    @abstractmethod
    def details(self):
        ...

