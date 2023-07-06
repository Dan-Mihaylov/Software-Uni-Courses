class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people) -> str or None:
        if not self.is_taken and people <= self.capacity - self.guests:
            self.is_taken = True
            self.guests += people
        else:
            return f"Room number {self.number} cannot be taken"

    def free_room(self) -> str or None:
        if self.is_taken:
            self.is_taken = not self.is_taken
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"
