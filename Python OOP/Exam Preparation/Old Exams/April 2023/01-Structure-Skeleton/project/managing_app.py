from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:

    _AVAILABLE_VEHICLES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: list = []       # Holds User Objects
        self.vehicles: list = []    # Holds Vehicle Objects
        self.routes: list = []      # Holds Route Objects

    def _find_user_by_driving_license_number(self, license_number: str):
        for user in self.users:
            if user.driving_license_number == license_number:
                return user
        return

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self._find_user_by_driving_license_number(driving_license_number) is not None:
            return f"{driving_license_number} has already been registered to our platform."
        else:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def _find_vehicle_by_license_plate(self, license_plate: str):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate:
                return vehicle
        return

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ("PassengerCar", "CargoVan"):
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self._find_vehicle_by_license_plate(license_plate_number) is not None:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self._AVAILABLE_VEHICLES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def _find_same_route_start_end_length(self, start, end, length):
        for route in self.routes:
            if route.start_point == start and route.end_point == end and route.length == length:
                return True
        return False

    def _find_same_route_shorter_length(self, start, end, length):
        for route in self.routes:
            if route.start_point == start and route.end_point == end:
                if route.length < length:
                    return True
                elif route.length > length:
                    route.is_locked = True
                return False
        return False

    def allow_route(self, start_point: str, end_point: str, length: float):

        if self._find_same_route_start_end_length(start_point, end_point, length):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if self._find_same_route_shorter_length(start_point, end_point, length):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        new_route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, new_route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def _find_route_by_id(self, id_number: int):
        for route in self.routes:
            if route.route_id == id_number:
                return route
        return

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self._find_user_by_driving_license_number(driving_license_number)
        vehicle = self._find_vehicle_by_license_plate(license_plate_number)
        route = self._find_route_by_id(route_id)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        ordered_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))
        if count < len(ordered_vehicles):
            for vehicle in ordered_vehicles[0:count]:
                vehicle.change_status()
                vehicle.recharge()
            return f"{count} vehicles were successfully repaired!"
        else:
            for vehicle in ordered_vehicles:
                vehicle.change_status()
                vehicle.recharge()
            return f"{len(ordered_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        users_ordered = sorted(self.users, key=lambda u: -u.rating)
        for user in users_ordered:
            result.append(user.__str__())

        return "\n".join(result)
