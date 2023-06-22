from project.person import Person


class Child(Person):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)


child = Child("Peter Jr", 5)
print(child.__class__.__bases__[0].__name__)
