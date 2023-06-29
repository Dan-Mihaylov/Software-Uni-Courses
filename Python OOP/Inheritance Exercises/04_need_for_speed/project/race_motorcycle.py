from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    # The bellow is not needed, since it will ask for all those details from the inherited class.
    # def __init__(self, fuel, horse_power):
    #     super().__init__(fuel, horse_power)
    #     Motorcycle.DEFAULT_FUEL_CONSUMPTION = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION
    #     self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION


race = RaceMotorcycle(100, 100)
print(race.fuel_consumption)
print(race.__class__.__bases__[0].__name__)
race.drive(10)
print(race.fuel)
