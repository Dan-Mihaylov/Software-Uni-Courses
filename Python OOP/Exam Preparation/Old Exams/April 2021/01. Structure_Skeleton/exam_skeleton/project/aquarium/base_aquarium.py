from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    @abstractmethod
    def type(self):
        pass

    # TODO maybe it will ask to return 0 if there is no decorations in.

    def calculate_comfort(self):
        result = 0

        for decoration in self.decorations:
            result += decoration.comfort

        return result

    def add_fish(self, fish):
        if fish.__class__.__name__ not in ("FreshwaterFish", "SaltwaterFish"):
            return

        if len(self.fish) == self.capacity:
            return f"Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f"{self.name}:",]

        result.append(f"Fish: {' '.join([f.name for f in self.fish]) if self.fish else 'none'}")
        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")
        return f"\n".join(result)

