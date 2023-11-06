from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


# 01 Restaurant
class Restaurant(models.Model):
    # Why Judge Did not accept the message as a variable?
    # MIN_NAME_VALUE_MESSAGE = "Name must be at least 2 characters long."
    # MAX_NAME_VALUE_MESSAGE = "Name cannot exceed 100 characters."
    # MIN_LOCATION_VALUE_MESSAGE = "Location must be at least 2 characters long."
    # MAX_LOCATION_VALUE_MESSAGE = "Location cannot exceed 200 characters."
    # MIN_RATING_MESSAGE = "Rating must be at least 0.00."
    # MAX_RATING_MESSAGE = "Rating cannot exceed 5.00."

    name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(limit_value=2, message="Name must be at least 2 characters long."),
            validators.MaxLengthValidator(limit_value=100, message="Name cannot exceed 100 characters."),
        ]
    )

    location = models.CharField(
        max_length=200,
        validators=[
            validators.MinLengthValidator(limit_value=2, message="Location must be at least 2 characters long."),
            validators.MaxLengthValidator(limit_value=200, message="Location cannot exceed 200 characters."),
        ]
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(limit_value=0, message="Rating must be at least 0.00."),
            validators.MaxValueValidator(limit_value=5, message="Rating cannot exceed 5.00."),
        ]
    )


# 02 Menu
def validate_menu_categories(values):
    if not all([value in values for value in ["Appetizers", "Main Course", "Desserts"]]):
        raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        validators=[
            validate_menu_categories,
        ]
    )

    restaurant = models.ForeignKey(
        "Restaurant",
        on_delete=models.CASCADE,
    )


# 03 Restaurant Review
# class RestaurantReview(models.Model):
#
#     class Meta:
#         ordering = ["-rating"]
#         verbose_name = "Restaurant Review"
#         verbose_name_plural = "Restaurant Reviews"
#         unique_together = ["reviewer_name", "restaurant"]
#
#
#     reviewer_name = models.CharField(
#         max_length=100,
#     )
#
#     restaurant = models.ForeignKey(
#         "Restaurant",
#         on_delete=models.CASCADE,
#     )
#
#     review_content = models.TextField()
#
#     rating = models.PositiveIntegerField(
#         validators=[
#             validators.MaxValueValidator(limit_value=5)
#         ]
#     )


# 06 Review Mixin
class ReviewMixin(models.Model):

    class Meta:
        ordering = ["-rating"]
        abstract = True

    reviewer_name = models.CharField(
        max_length=100,
    )

    review_content = models.TextField()



# 04 Restaurant Review Types
class RestaurantReview(ReviewMixin):

    class Meta(ReviewMixin.Meta):
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ["reviewer_name", "restaurant"]


    restaurant = models.ForeignKey(
        "Restaurant",
        on_delete=models.CASCADE,
    )


    rating = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(limit_value=5)
        ]
    )


class RegularRestaurantReview(RestaurantReview):
    pass


class FoodCriticRestaurantReview(RestaurantReview):

    class Meta(RestaurantReview.Meta):
        ordering = ["-rating"]
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"

    food_critic_cuisine_area = models.CharField(
        max_length=100
    )


# 05 Menu Review
class MenuReview(ReviewMixin):

    class Meta(ReviewMixin.Meta):
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ["reviewer_name", "menu"]
        indexes = [
            models.Index(fields=["menu"], name="main_app_menu_review_menu_id"),
        ]

    menu = models.ForeignKey(
        "Menu",
        on_delete=models.CASCADE,
        db_index=True,
    )

    rating = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(limit_value=5,)
        ]
    )




