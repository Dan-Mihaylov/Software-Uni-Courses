from django.db import models
from django.core import validators
from .validators import username_char_validator


class Profile(models.Model):
    MAX_USERNAME_LENGTH=15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            username_char_validator,
            validators.MinLengthValidator(2)
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(0),
        ],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username

