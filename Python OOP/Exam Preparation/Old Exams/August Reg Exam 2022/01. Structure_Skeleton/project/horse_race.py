class HorseRace:
    _VALID_TYPES = ("Winter", "Spring", "Autumn", "Summer")

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys: list = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value: str):
        if value not in self._VALID_TYPES:
            raise ValueError("Race type does not exist!")

        self.__race_type = value

