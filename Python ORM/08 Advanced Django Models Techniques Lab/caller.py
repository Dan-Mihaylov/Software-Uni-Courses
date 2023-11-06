import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from django.core.exceptions import ValidationError
from main_app.models import (
    Restaurant, Menu, RestaurantReview, RegularRestaurantReview, FoodCriticRestaurantReview,
    MenuReview,

)

