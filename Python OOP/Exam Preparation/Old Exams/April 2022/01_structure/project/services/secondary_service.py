from project.services.base_service import BaseService


class SecondaryService(BaseService):
    INITIAL_CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.INITIAL_CAPACITY)

    def details(self):
        result = [f"{self.name} Secondary Service:"]

        result.append(f"Robots: {' '.join(x.name for x in self.robots) if self.robots else 'none'}")

        return f"\n".join(result)

