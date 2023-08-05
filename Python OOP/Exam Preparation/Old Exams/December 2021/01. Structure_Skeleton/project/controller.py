from project.car.sports_car import SportsCar
from project.car.muscle_car import MuscleCar
from project.race import Race
from project.driver import Driver
from project.car.car import Car
from typing import List


class Controller:
    __ALLOWED_CAR_TYPES = ("MuscleCar", "SportsCar")
    __CAR_MAPPER = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def _find_car_by_model(self, model: str) -> Car or None:
        for car in self.cars:
            if car.model == model:
                return car
        return None

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.__ALLOWED_CAR_TYPES:
            return

        if self._find_car_by_model(model) is not None:
            raise Exception(f"Car {model} is already created!")

        new_car = self.__CAR_MAPPER[car_type](model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def _find_driver_by_name(self, name: str) -> Driver or None:
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def create_driver(self, driver_name: str):
        if self._find_driver_by_name(driver_name) is not None:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def _find_race_by_name(self, race_name: str) -> Race or None:
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def create_race(self, race_name: str):
        if self._find_race_by_name(race_name) is not None:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def _find_car_by_type(self, car_type: str) -> Car or None:
        for i in range(len(self.cars) - 1, -1, -1):
            if self.cars[i].type() == car_type and not self.cars[i].is_taken:
                return self.cars[i]
        return None

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self._find_driver_by_name(driver_name)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        found_car = self._find_car_by_type(car_type)
        if found_car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is None:
            found_car.is_taken = True
            driver.car = found_car
            return f"Driver {driver_name} chose the car {found_car.model}."

        if driver.car is not None:
            old_model = driver.car.model
            old_car = self._find_car_by_model(old_model)
            old_car.is_taken = False
            new_model = found_car.model
            driver.car = found_car
            found_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

    @staticmethod
    def _check_if_driver_is_already_in_race(race: Race, driver_name: str):
        for driver in race.drivers:
            if driver.name == driver_name:
                return True
        return False

    def add_driver_to_race(self, race_name: str, driver_name: str):
        found_race = self._find_race_by_name(race_name)
        if found_race is None:
            raise Exception(f"Race {race_name} could not be found!")

        found_driver = self._find_driver_by_name(driver_name)
        if found_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if found_driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if self._check_if_driver_is_already_in_race(found_race, driver_name):
            return f"Driver {driver_name} is already added in {race_name} race."

        found_race.drivers.append(found_driver)
        return f"Driver {driver_name} added in {race_name} race."

    @staticmethod
    def _find_3_winners(race: Race) -> [Driver] * 3:
        winners = list(sorted(race.drivers, key=lambda driver: -driver.car.speed_limit))
        return winners[:3]

    def start_race(self, race_name: str):
        found_race = self._find_race_by_name(race_name)
        if found_race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(found_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = self._find_3_winners(found_race)

        result = []

        for driver in winners:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)



