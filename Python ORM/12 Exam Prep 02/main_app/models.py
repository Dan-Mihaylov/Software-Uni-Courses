from django.db import models
from django.core import validators
from .managers import ProfileManager


class CreationDateMixin(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Profile(CreationDateMixin, models.Model):

    full_name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(2)
        ],
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15
    )

    address = models.TextField()
    is_active = models.BooleanField(default=True)

    objects = ProfileManager()

    def __str__(self):
        return f"{self.full_name}"


class Product(CreationDateMixin, models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validators.MinValueValidator(0.01)],
    )
    in_stock = models.PositiveIntegerField(validators=[validators.MinValueValidator(0)])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Order(CreationDateMixin, models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, related_name='orders')
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.01)
        ],
    )
    is_completed = models.BooleanField(default=False)




