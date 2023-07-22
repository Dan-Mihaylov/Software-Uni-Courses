from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.vet import Vet
from project.caretaker import Caretaker
from project.keeper import Keeper


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker_filtered = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker_filtered)
            return f"{worker_name} fired successfully"

        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion_count = [0]
        tiger_count = [0]
        cheetah_count = [0]
        total_animals = len(self.animals)
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lion_count[0] += 1
                lion_count.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tiger_count[0] += 1
                tiger_count.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetah_count[0] += 1
                cheetah_count.append(animal)
        result = [f"You have {total_animals} animals", f"----- {lion_count[0]} Lions:"]
        [result.append(x.__repr__()) for x in lion_count[1:]]
        result.append(f"----- {tiger_count[0]} Tigers:")
        [result.append(x.__repr__()) for x in tiger_count[1:]]
        result.append(f"----- {cheetah_count[0]} Cheetahs:")
        [result.append(x.__repr__()) for x in cheetah_count[1:]]

        return "\n".join(result)

    def workers_status(self):
        total_workers = len(self.workers)
        keepers_count = [0]
        caretakers_count = [0]
        vets_count = [0]

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers_count[0] += 1
                keepers_count.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers_count[0] += 1
                caretakers_count.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets_count[0] += 1
                vets_count.append(worker)

        result = [f"You have {total_workers} workers", f"----- {keepers_count[0]} Keepers:"]
        [result.append(x.__repr__()) for x in keepers_count[1:]]
        result.append(f"----- {caretakers_count[0]} Caretakers:")
        [result.append(x.__repr__()) for x in caretakers_count[1:]]
        result.append(f"----- {vets_count[0]} Vets:")
        [result.append(x.__repr__()) for x in vets_count[1:]]

        return f"\n".join(result)

