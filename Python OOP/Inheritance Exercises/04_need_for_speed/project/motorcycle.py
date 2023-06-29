from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = Vehicle.DEFAULT_FUEL_CONSUMPTION

    # def __init__(self, fuel, horse_power):
    #     super().__init__(fuel, horse_power)
    #     Vehicle.DEFAULT_FUEL_CONSUMPTION = Motorcycle.DEFAULT_FUEL_CONSUMPTION
    #     self.fuel_consumption = Motorcycle.DEFAULT_FUEL_CONSUMPTION


# moto = Motorcycle(50, 50)
# print(moto.fuel_consumption)
# moto.drive(10)
# print(moto.fuel)
