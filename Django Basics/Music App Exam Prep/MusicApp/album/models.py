from django.core import validators
from django.db import models

from MusicApp.account.models import Profile


class Album(models.Model):
    MAX_CHAR_FIELD_LENGTH = 30
    GENRE_CHOICES = (
        ('Pop', 'Pop Music'),
        ('Jazz', 'Jazz Music'),
        ('R&B', 'R&B Music'),
        ('Rock', 'Rock Music'),
        ('Country', 'Country Music'),
        ('Dance', 'Dance Music'),
        ('Hip Hop', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    album_name = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        choices=GENRE_CHOICES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(0),
        ],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        Profile,
        # TODO on delete
        on_delete=models.CASCADE,
        related_name='albums',
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.album_name