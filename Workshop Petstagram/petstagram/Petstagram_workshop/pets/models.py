from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    NAME_MAXLENGTH = 30

    name = models.CharField(
        max_length=NAME_MAXLENGTH
    )

    photo = models.URLField(
        blank=False,
        null=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    added_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
