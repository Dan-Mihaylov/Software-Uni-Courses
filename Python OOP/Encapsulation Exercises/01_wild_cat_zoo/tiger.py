from project.animal import Animal


class Tiger(Animal):
    __MONEY_TO_CARE = 45

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender, money_for_care=Tiger.__MONEY_TO_CARE)
