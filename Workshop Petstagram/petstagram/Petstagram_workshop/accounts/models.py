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

