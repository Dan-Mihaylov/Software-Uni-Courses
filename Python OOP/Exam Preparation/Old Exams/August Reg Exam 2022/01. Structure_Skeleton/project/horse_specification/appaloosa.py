from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    def max_speed(self):
        return 120

    def type(self):
        return self.__class__.__name__



