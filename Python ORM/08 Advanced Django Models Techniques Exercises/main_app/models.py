from decimal import Decimal


from django.db import models
from .validators import (
    customer_name_validator, phone_number_validator, min_age_validator,
)
from django.core import validators
from django.contrib.postgres.search import SearchVectorField


# 01 Customer
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            customer_name_validator,
            validators.MaxLengthValidator(limit_value=100)
        ]
    )

    age = models.PositiveIntegerField(
        validators=[
            min_age_validator,
        ]
    )

    email = models.EmailField(
        validators=[
            validators.EmailValidator,
        ]
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[
            phone_number_validator,
        ]
    )

    website_url = models.URLField(
        validators=[
            validators.URLValidator
        ]
    )


# 02 Media
class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ["-created_at", "title"]

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"

    author = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(limit_value=5, message="Author must be at least 5 characters long")
        ],
    )
    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            validators.MinLengthValidator(limit_value=6, message="ISBN must be at least 6 characters long")
        ],
    )


class Movie(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"

    director = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(limit_value=8, message="Director must be at least 8 characters long")
        ],
    )


class Music(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"

    artist = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(limit_value=9, message="Artist must be at least 9 characters long")
        ],
    )


# 03 Digital Products
class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        percentage = Decimal(0.08)
        tax_paid = self.price * percentage
        return tax_paid

    def calculate_shipping_cost(self, weight: Decimal):
        return weight * Decimal(2.00)

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):

    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        price_without_discount = self.price * Decimal(1.2)
        return price_without_discount

    def calculate_tax(self):
        tax = self.price * Decimal(0.05)
        return tax

    def calculate_shipping_cost(self, weight: Decimal):
        shipping_cost = weight * Decimal(1.5)
        return shipping_cost

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


# 04 SuperHero Universe
class RechargeEnergyMixin:

    def recharge_energy(self, amount: int):
        self.energy = min(self.energy + amount, 100)
        self.save()


class Hero(models.Model, RechargeEnergyMixin):

    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    ENERGY_NEEDED_FOR_SKILL = 80

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        self.energy -= self.ENERGY_NEEDED_FOR_SKILL
        if self.energy <= 0:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        else:
            self.save()
            return f"{self.name} as Spider Hero swings from buildings using web shooters"



class FlashHero(Hero):

    ENERGY_NEEDED_FOR_SKILL = 65
    class Meta:
        proxy = True

    def run_at_super_speed(self):
        self.energy -= self.ENERGY_NEEDED_FOR_SKILL
        if self.energy <= 0:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        else:
            self.save()
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"


# 05 Vector Searching
class Document(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['search_vector'], name="search_vector_field_index")
        ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(null=True)
