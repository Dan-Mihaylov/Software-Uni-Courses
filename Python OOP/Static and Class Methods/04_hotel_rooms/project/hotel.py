from typing import List

from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        try:
            room = next(filter(lambda r_n: r_n.number == room_number ,self.rooms))
            if room.take_room(people) is None:
                self.guests += people
        except StopIteration:
            pass

    def free_room(self, room_number: int):
        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            guests = room.guests
            if room.free_room() is None:
                self.guests -= guests
        except StopIteration:
            pass

    def status(self):
        result = [f"Hotel {self.name} has {self.guests} total guests"]

        free_rooms = list(filter(lambda r: not r.is_taken, self.rooms))
        taken_rooms = list(filter(lambda r: r.is_taken, self.rooms))

        result.append(f"Free rooms: {', '.join(str(x.number) for x in free_rooms)}")
        result.append(f"Taken rooms: {', '.join(str(x.number) for x in taken_rooms)}")

        return "\n".join(result)




