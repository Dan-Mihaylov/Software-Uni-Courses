from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 180.00)

    def drive(self, mileage: float):

        self.battery_level -= (round(mileage / 180.00 * 100) + 5)

        # TODO do you do the rounding before or after you have calculated the percentage plus the additional 5%
