from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from abc import ABC, abstractmethod


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []    # [FemaleRobot, MaleRobot ...]

    @abstractmethod
    def details(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or all([l == " " for l in value]):
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value