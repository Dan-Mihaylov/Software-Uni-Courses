from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from typing import List
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish



class Controller:
    _AQUARIUMS = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    _DECORATIONS = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    _FISH = {
        "SaltwaterFish": SaltwaterFish,
        "FreshwaterFish": FreshwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self._AQUARIUMS:
            return f"Invalid aquarium type."

        aquarium = self._AQUARIUMS[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self._DECORATIONS:
            return f"Invalid decoration type."

        decoration = self._DECORATIONS[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def _find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium
        return None

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        found_aquarium = self._find_aquarium_by_name(aquarium_name)
        found_decor = self.decorations_repository.find_by_type(decoration_type)

        if found_aquarium is not None and found_decor != "None":
            found_aquarium.add_decoration(found_decor)
            self.decorations_repository.remove(found_decor)
            return f"Successfully added {decoration_type} to {aquarium_name}."

        if found_decor == "None":
            return f"There isn't a decoration of type {decoration_type}."


    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self._FISH:
            return f"There isn't a fish of type {fish_type}."

        found_aquarium = self._find_aquarium_by_name(aquarium_name)
        new_fish = self._FISH[fish_type](fish_name, fish_species, price)
        if (fish_type == "SaltwaterFish" and found_aquarium.__class__.__name__ != "SaltwaterAquarium")\
                or (fish_type == "FreshwaterFish" and found_aquarium.__class__.__name__ != "FreshwaterAquarium"):
            return f"Water not suitable."

        else:
            result = found_aquarium.add_fish(new_fish)
            return result

    def feed_fish(self, aquarium_name: str):
        found_aquarium = self._find_aquarium_by_name(aquarium_name)
        found_aquarium.feed()
        return f"Fish fed: {len(found_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        found_aquarium = self._find_aquarium_by_name(aquarium_name)
        total = 0
        for fish in found_aquarium.fish:
            total += fish.price

        for decor in found_aquarium.decorations:
            total += decor.price

        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        result = []

        for aquarium in self.aquariums:
            result.append(str(aquarium))

        return f"\n".join(result)

