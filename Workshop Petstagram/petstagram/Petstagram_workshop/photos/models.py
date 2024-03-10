from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram_workshop.pets.models import Pet
from Petstagram_workshop.photos.validators import validate_file_size

from django.contrib.auth import get_user_model


MAX_LENGTH_TEXT_FIELD = 300
MAX_LENGTH_CHAR_FIELD = 30

UserModel = get_user_model()


class Photo(models.Model):

    user = models.ForeignKey(
        UserModel,
        related_name='photos',
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    photo = models.ImageField(
        upload_to='mediafiles/',
        validators=(validate_file_size,),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_LENGTH_TEXT_FIELD,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LENGTH_CHAR_FIELD,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        related_name='photos'
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=False,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    def __str__(self):

        return f'{self.id} - {", ".join([pet.name for pet in self.tagged_pets.all()])}'


class Comment(models.Model):

    class Meta:
        ordering = ['-added_on']

    text = models.TextField(
        max_length=MAX_LENGTH_TEXT_FIELD,
        blank=False,
        null=False,
    )

    added_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    to_photo = models.ForeignKey(
        Photo,
        related_name='comments',
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        related_name='comments',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=False,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        related_name='likes',
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        related_name='likes',
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

