from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self) -> None:
        pass

    @abstractmethod
    def refuel(self) -> None:
        pass


class Car(Vehicle):

    AIR_CON_ON = 0.9

    def drive(self, distance: float) -> None:
        consumption =  (self.fuel_consumption + Car.AIR_CON_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):

    AIR_CON_ON = 1.6
    FUEL_KEEP = 0.95

    def drive(self, distance: float) -> None:
        consumption = (self.fuel_consumption + Truck.AIR_CON_ON) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.FUEL_KEEP




car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
