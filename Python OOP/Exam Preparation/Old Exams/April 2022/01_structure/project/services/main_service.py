from project.services.base_service import BaseService


class MainService(BaseService):

    INITIAL_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.INITIAL_CAPACITY)

    def details(self):
        result = [f"{self.name} Main Service:"]

        result.append(f"Robots: {' '.join(x.name for x in self.robots) if self.robots else 'none'}")

        return f"\n".join(result)

