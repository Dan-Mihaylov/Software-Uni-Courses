from project.animal import Animal


class Lion(Animal):
    __MONEY_TO_CARE = 50

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender, money_for_care=Lion.__MONEY_TO_CARE)
