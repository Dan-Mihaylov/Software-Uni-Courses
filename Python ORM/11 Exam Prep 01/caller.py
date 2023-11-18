import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Director, Movie, Actor
from django.db.models import Q, F


def get_directors(search_name=None, search_nationality=None):

    if all([arg is None for arg in [search_name, search_nationality]]):
        return ""

    query = Q(full_name__icontains=search_name) | Q(nationality__icontains=search_nationality)

    # TODO Need a break


# actor = Actor()
# movie = Movie.objects.all().first()
# movie.actors.add(actor)

# print(Actor.objects.all())
# print(Movie.objects.all())
# # print(Movie.objects.all().first().actors.add(Actor.objects.all().first()))
# print(Movie.objects.all().first().actors.all().first().full_name)

