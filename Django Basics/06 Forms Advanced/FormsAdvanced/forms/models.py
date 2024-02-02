from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from .validators import validate_space_in_name


class Person(models.Model):
    MIN_NAMES_LENGTH = 3
    MAX_NAMES_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAMES_LENGTH),
            validate_space_in_name,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_NAMES_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAMES_LENGTH),
            validate_space_in_name,
        ),
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to='forms/profile_images',
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True\
    )