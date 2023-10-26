import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# 01 Pet
def create_pet(name_: str, species_: str):
    Pet.objects.create(name=name_, species=species_)
    return f"{name_} is a very cute {species_}!"


# print(create_pet("Buddy", "Dog"))
# print(create_pet("Whiskers", "Cat"))
# print(create_pet("Rocky", "Hamster"))


# 02 Artifact
def create_artifact(name_: str, origin_: str, age_: int, description_: str, is_magical_: bool):
    Artifact.objects.create(name=name_, origin=origin_, age=age_, description=description_, is_magical=is_magical_)
    return f"The artifact {name_} is {age_} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
#
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))


# 03 Location

def show_all_locations():
    result = []

    for location in Location.objects.all().order_by("-id"):
        result.append(
            f"{location.name} has a population of {location.population}!"
        )
    return "\n".join(result)


# print(show_all_locations())


def new_capital():
    new_capital = Location.objects.first()
    new_capital.is_capital = True
    new_capital.save()


# new_capital()


def get_capitals():
    return Location.objects.all().filter(is_capital=True).values("name")


# print(get_capitals())


def delete_first_location():
    Location.objects.first().delete()


# delete_first_location()


#04 Car

def apply_discount():

    for car in Car.objects.all():
        year = str(car.year)
        percentage = 0

        for digit in year:
            percentage += int(digit)

        percentage /= 100

        current_price = float(car.price)
        car.price_with_discount = (1 - percentage) * current_price
        car.save()


# apply_discount()


def get_recent_cars():
    return Car.objects.all().filter(year__gte=2020).values("model", "price_with_discount")


# print(get_recent_cars())


def delete_last_car():
    Car.objects.last().delete()


# 05 Task Encoder

def show_unfinished_tasks():
    result = []
    for task in Task.objects.all().filter(is_finished=False):
        result.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return "\n".join(result)


# print(show_all_unfinished_tasks())


def complete_odd_tasks():

    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


# complete_odd_tasks()


def encode_and_replace(text: str, task_title_: str):
    decoded_text = ""
    for char in text:
        decoded_text += chr(ord(char) - 3)

    for task in Task.objects.all().filter(title=task_title_):
        task.description = decoded_text
        task.save()


# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
# print(Task.objects.get(title ='Simple Task') .description)

# 06 Hotel Room

def get_deluxe_rooms():
    result = []

    for room in HotelRoom.objects.all().filter(room_type="Deluxe"):
        if room.id % 2 == 0:
            result.append(f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!")

    return "\n".join(result)


# print(get_deluxe_rooms())


def increase_room_capacity():
    prev = HotelRoom.objects.first().id

    for room in HotelRoom.objects.all().order_by("id"):
        if room.is_reserved:
            room.capacity = room.capacity + prev
            room.save()
        prev = room.capacity


# increase_room_capacity()


def reserve_first_room():
    first = HotelRoom.objects.first()
    first.is_reserved = True
    first.save()


# reserve_first_room()


def delete_last_room():
    last = HotelRoom.objects.last()
    if last.is_reserved:
        last.delete()


# delete_last_room()