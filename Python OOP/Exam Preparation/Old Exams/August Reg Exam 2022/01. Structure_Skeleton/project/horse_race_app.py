from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace
from typing import List


class HorseRaceApp:
    _AVAILABLE_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Thoroughbred, Appaloosa] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def _find_horse_by_name(self, name: str):
        for horse in self.horses:
            if horse.name == name:
                return horse
        return None

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self._AVAILABLE_HORSE_TYPES:
            return

        if self._find_horse_by_name(horse_name) is not None:
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self._AVAILABLE_HORSE_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def _find_jockey_by_name(self, name: str):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey
        return None

    def add_jockey(self, jockey_name: str, age: int):
        if self._find_jockey_by_name(jockey_name) is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def _find_horse_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def create_horse_race(self, race_type: str):
        if self._find_horse_race_by_type(race_type) is not None:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def _find_available_horse_by_type(self, horse_type: str):
        for index in range(len(self.horses) - 1, -1, -1):
            horse = self.horses[index]
            if horse.type() == horse_type and not horse.is_taken:
                return horse
        return None

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        jockey = self._find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self._find_available_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    @staticmethod
    def _find_if_jockey_already_in_race_by_jockey_name(horse_race: HorseRace, jockey_name: str):
        for jockeys in horse_race.jockeys:
            if jockeys.name == jockey_name:
                return True
        return False

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        horse_race = self._find_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self._find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if self._find_if_jockey_already_in_race_by_jockey_name(horse_race, jockey_name):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    @staticmethod
    def _find_winner_in_horse_race(horse_race: HorseRace):
        found_jockey = None
        max_speed = 0

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                found_jockey = jockey

        return found_jockey

    def start_horse_race(self, race_type: str):

        horse_race = self._find_horse_race_by_type(race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self._find_winner_in_horse_race(horse_race)
        horse = winner.horse

        return f"The winner of the {race_type} race, with a speed of {horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {horse.name}."

