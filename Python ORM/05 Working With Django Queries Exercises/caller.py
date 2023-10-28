import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ArtworkGallery, Meal, ChessPlayer, Dungeon, Workout, Laptop


# 01 Artwork
def show_highest_rated_art() -> str:
    highest_rated = ArtworkGallery.objects.all().order_by("-rating", "id").first()
    return f"{highest_rated.art_name} is the highest-rated art with {highest_rated.rating} rating!"


def bulk_create_arts(first_object, second_object) -> None:
    ArtworkGallery.objects.bulk_create([
        first_object,
        second_object
    ])


def delete_negative_rated_arts() -> None:
    negative_rated = ArtworkGallery.objects.exclude(rating__gte=0)
    negative_rated.delete()


# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
#
#
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())

# 02 Laptop

def show_the_most_expensive_laptop():
    most_expensive = Laptop.objects.all().order_by("-price", "id").first()
    return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    laptops_to_update = Laptop.objects.filter(brand__in=["Asus", "Apple", "Dell", "Lenovo"])

    for laptop in laptops_to_update:
        if laptop.brand == "Asus":
            laptop.operation_system = "Windows"
        elif laptop.brand == "Apple":
            laptop.operation_system = "MacOS"
        elif laptop.brand == "Dell":
            laptop.operation_system = "Linux"
        elif laptop.brand == "Lenovo":
            laptop.operation_system = "Chrome OS"
        laptop.save()

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


