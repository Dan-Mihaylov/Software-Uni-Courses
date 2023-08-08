from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots = []    # list with robots obj
        self.services = []  # list with services obj

    def add_service(self, service_type: str, name: str):
        service = None

        if service_type == "MainService":
            service = MainService(name)
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
        else:
            raise Exception("Invalid service type!")

        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        robot = None

        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
        else:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        find_robot = next(filter(lambda r: r.name == robot_name, self.robots))
        find_service = next(filter(lambda s: s.name == service_name, self.services))

        if (type(find_robot) == "FemaleRobot" and type(find_service) == "MainService")\
            or (type(find_robot) == "MaleRobot" and type(find_service) == "SecondaryService"):
            return "Unsuitable service"
        elif not len(find_service.robots) < find_service.capacity:
            raise Exception("Not enough capacity for this robot!")
        else:
            self.robots.remove(find_robot)
            find_service.robots.append(find_robot)
            return f"Successfully added {find_robot.name} to {find_service.name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        find_service = next(filter(lambda s: s.name == service_name, self.services))
        found_robot = [x for x in find_service.robots if x.name == robot_name]
        if len(found_robot) == 0:
            raise Exception("No such robot in this service!")
        else:
            self.robots.append(found_robot[0])
            find_service.robots.remove(found_robot[0])
            return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        find_service = next(filter(lambda s: s.name == service_name, self.services))

        for robot in find_service.robots:
            robot.eating()

        return f"Robots fed: {len(find_service.robots)}."

    def service_price(self, service_name: str):
        find_service = next(filter(lambda s: s.name == service_name, self.services))
        total = 0

        for robot in find_service.robots:
            total += robot.price

        return f"The value of service {service_name} is {total:.2f}."

    def __str__(self):
        result = []

        for service in self.services:
            result.append(service.details())

        return f"\n".join(result)



