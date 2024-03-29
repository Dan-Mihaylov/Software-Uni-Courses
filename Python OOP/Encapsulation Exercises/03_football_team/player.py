class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        info = {
            "Player: ": self.__name,
            "Sprint: ": self.__sprint,
            "Dribble: ": self.__dribble,
            "Passing: ": self.__passing,
            "Shooting: ": self.__shooting
        }
        result = []
        for description, value in info.items():
            result.append(f"{description}{value}")

        return "\n".join(result)
