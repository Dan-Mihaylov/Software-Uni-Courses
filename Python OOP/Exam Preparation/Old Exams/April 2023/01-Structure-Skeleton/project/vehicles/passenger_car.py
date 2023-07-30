from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 450.00)

    def drive(self, mileage: float):
        self.battery_level -= round(mileage / 450.00 * 100)

    # TODO CHECK IF BATTERY LEVEL CANNOT GO UNDER 0 PERCENT, MAYBE THERE IS ANOTHER METHOD LATER ON TO RAISE

