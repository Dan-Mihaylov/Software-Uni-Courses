from project.car import Car


class FamilyCar(Car):
    pass
    # DEFAULT_FUEL_CONSUMPTION = Car.DEFAULT_FUEL_CONSUMPTION
    #
    # def __init__(self, fuel, horse_power):
    #     super().__init__(fuel, horse_power)
    #     self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION

    # def drive(self, kilometers):
    #     if self.fuel_consumption * kilometers <= self.fuel:
    #         self.fuel -= self.fuel_consumption * kilometers

# print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
# family_car = FamilyCar(150, 150)
# family_car.drive(50)
# print(family_car.fuel)
# family_car.drive(50)
# print(family_car.fuel)
# print(family_car.__class__.__bases__[0].__name__)
