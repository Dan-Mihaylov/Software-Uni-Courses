from project.supply.supply import Supply


class Player:
    players_names = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:

        if value == '':
            raise ValueError("Name not valid!")

        elif value in Player.players_names:
            raise Exception(f"Name {value} is already used!")

        Player.players_names.append(value)
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value) -> None:

        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self) -> int or float:
        return self.__stamina

    @stamina.setter
    def stamina(self, value) -> None:

        if value < 0 or 100 < value:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self) -> bool:
        return self.__stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
