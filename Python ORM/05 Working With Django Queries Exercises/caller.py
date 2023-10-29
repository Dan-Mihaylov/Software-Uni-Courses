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

def show_the_most_expensive_laptop() -> str:
    most_expensive = Laptop.objects.all().order_by("-price", "id").first()
    return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"


def bulk_create_laptops(*args) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
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

def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# 03 Chess Player

def bulk_create_chess_players(*args) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title__isnull=True).update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")


# 04 Meal


def set_new_chefs() -> None:
    Meal.objects.filter(meal_type="Breakfast").update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type="Lunch").update(chef="Julia Child")
    Meal.objects.filter(meal_type="Dinner").update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type="Snack").update(chef="Thomas Keller")


def set_new_preparation_times() -> None:
    Meal.objects.filter(meal_type="Breakfast").update(preparation_time="10 minutes")
    Meal.objects.filter(meal_type="Lunch").update(preparation_time="12 minutes")
    Meal.objects.filter(meal_type="Dinner").update(preparation_time="15 minutes")
    Meal.objects.filter(meal_type="Snack").update(preparation_time="5 minutes")


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=["Breakfast", "Dinner"]).update(calories=400) # Correct in Judge


def update_high_calorie_meals() -> None:
    # Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700) # Not Correct in Judge

    meals = Meal.objects.filter(meal_type__in=("Lunch", "Snack"))   # Correct in Judge

    for meal in meals:
        meal.calories = 700
        meal.save()


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()



