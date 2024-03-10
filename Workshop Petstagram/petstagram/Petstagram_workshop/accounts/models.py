from django.db import models
from django.contrib.auth import models as auth_models

from .managers import PetstagramUserManager

a = auth_models.AbstractUser


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PetstagramUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    FIRST_NAME_MAXLENGTH = 30
    LAST_NAME_MAXLENGTH = 30

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAXLENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAXLENGTH,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def get_name(self):

        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name or self.user.email

    def __str__(self):
        return self.user.email
