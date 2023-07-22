from project.animal import Animal


class Cheetah(Animal):
    __MONEY_TO_CARE = 60

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender, money_for_care=Cheetah.__MONEY_TO_CARE)
