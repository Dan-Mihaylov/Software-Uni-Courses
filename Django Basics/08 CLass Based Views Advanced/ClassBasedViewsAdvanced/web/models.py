from django.core import validators
from django.db import models


class Car(models.Model):
    ENGINE_CHOICES = (
        ('P', 'Petrol'),
        ('D', 'Diesel'),
        ('H', 'Hybrid'),
        ('E', 'Electric'),
        (None, None),
    )

    make = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    engine_type = models.CharField(
        max_length=15,
        choices=ENGINE_CHOICES,
        null=False,
        blank=False,
    )

    year = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1890, 'Value must be bigger than 1889'),
            validators.MaxValueValidator(2024, 'Value cannot be bigger than 2024'),
        ],
        null=False,
        blank=False,
    )

    added_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True,
    )

