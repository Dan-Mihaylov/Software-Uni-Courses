import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ArtworkGallery, Meal, ChessPlayer, Dungeon, Workout, Laptop
from django.db.models import QuerySet, Q, Case, When, Value


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
    # Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)

    # With Q object  (   | -> OR,   & -> AND   )

    Laptop.objects.filter(Q(brand="Lenovo") | Q(brand="Asus")).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)

    # With Q object

    # Laptop.objects.filter(Q(brand="Apple") | Q(brand="Dell") | Q(brand="Acer")).update(memory=16)


def update_operation_systems() -> None:

    # With Cases Optimization to do only one DB hit.

    Laptop.objects.update(
        operation_system = Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand__in=("Dell", "Acer"),then=Value("Linux")),
            When(brand="Lenovo", then=Value("Chrome OS")),
        )
    )

    # laptops_to_update = Laptop.objects.filter(brand__in=["Asus", "Apple", "Dell", "Lenovo"])
    #
    # for laptop in laptops_to_update:
    #     if laptop.brand == "Asus":
    #         laptop.operation_system = "Windows"
    #     elif laptop.brand == "Apple":
    #         laptop.operation_system = "MacOS"
    #     elif laptop.brand == "Dell":
    #         laptop.operation_system = "Linux"
    #     elif laptop.brand == "Lenovo":
    #         laptop.operation_system = "Chrome OS"
    #     laptop.save()

    # Optimization with Dictionary

    # OS_INFO ={
    #     "Apple": "Mac OS",
    #     "Asus": "Windows",
    #     "Dell": "Linux",
    #     "Acer": "Linux",
    #     "Lenovo": "Chrome OS"
    # }
    #
    # Laptop.objects.filter(brand__in=["Apple", "Asus", "Dell", "Acer", "Lenovo"]).update(operation_system=OS_INFO[Laptop.brand])

def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# 03 Chess Player

def bulk_create_chess_players(*args) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    # get the titles from the meta fields
    # model.__meta.fields
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

    # With Q
    # ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating__lte=2399)).update(title="IM")


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


# 05 Dungeon


def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty="Hard").order_by("-location")
    result = [
        f"{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!"
        for dungeon in hard_dungeons
        ]
    return "\n".join(result)


def bulk_create_dungeons(*args) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    # Solution With 3 Filters

    # Dungeon.objects.filter(difficulty="Easy").update(name="The Erased Thombs")
    # Dungeon.objects.filter(difficulty="Medium").update(name="The Coral Labyrinth")
    # Dungeon.objects.filter(difficulty="Hard").update(name="The Lost Haunt")

    # Optimization with Case, that will have only one query req to the database.
    Dungeon.objects.filter(
        Case(
            When(dificulty="Easy", then=Value("The Erased Thombs")),
            When(dificulty="Medium", then=Value("The Coral Labyrinth")),
            When(dificulty="Hard", then=Value("The Lost Haunt")),
        )
    )

    # Solution with if else getting all objects from the database.

    # dungeons = Dungeon.objects.all()
    #
    # for dungeon in dungeons:
    #     if dungeon.difficulty == "Easy":
    #         dungeon.name = "The Erased Thombs"
    #     elif dungeon.difficulty == "Medium":
    #         dungeon.name = "The Coral Labyrinth"
    #     elif dungeon.difficulty == "Hard":
    #         dungeon.name = "The Lost Haunt"
    #     dungeon.save()


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    # dungeons = Dungeon.objects.all()
    #
    # for dungeon in dungeons:
    #     if dungeon.difficulty == "Easy":
    #         dungeon.recommended_level = 25
    #     elif dungeon.difficulty == "Medium":
    #         dungeon.recommended_level = 50
    #     elif dungeon.difficulty == "Hard":
    #         dungeon.recommended_level = 75
    #     dungeon.save()

    # Optimized code with Cases
    Dungeon.objects.filter(
        Case(
            When(difficulty= "Easy", then=Value(recommended_level=25)),
            When(difficulty= "Medium", then=Value(recommended_level=50)),
            When(difficulty="Hard", then=Value(recommended_level=75)),
        )
    )


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations() -> None:
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


# 06 Workout


def show_workouts() -> str:
    workouts_information = [
        f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!"
        for workout in Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"])
    ]
    return "\n".join(workouts_information)


def get_high_difficulty_cardio_workouts() -> QuerySet:
    return Workout.objects.filter(workout_type="Cardio").filter(difficulty="High").order_by("instructor")


def set_new_instructors() -> None:
    Workout.objects.filter(workout_type="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type="Calisthenics").update(instructor="Chris Heria")


def set_new_duration_times() -> None:
    Workout.objects.filter(instructor__exact="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor__exact="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor__exact="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor__exact="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor__exact="Emily Johnson").update(duration="1 hour and 30 minutes")


def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()
