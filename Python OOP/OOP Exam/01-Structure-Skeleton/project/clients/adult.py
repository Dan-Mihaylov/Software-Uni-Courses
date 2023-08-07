from project.clients.base_client import BaseClient


class Adult(BaseClient):
    _INITIAL_RATE = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Adult._INITIAL_RATE)

    def increase_clients_interest(self):
        self.interest += 2.0

