from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


# 01
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    # 06 Animals Age
    @property
    def age(self):
        calculate_age = date.today().year - self.birth_date.year - (
            (date.today().month, date.today().day) < (self.birth_date.month, self.birth_date.day)
        )

        return calculate_age


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


# 02
class Employee(models.Model):

    class Meta:
        abstract = True

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)


class ZooKeeper(Employee):

    class SpecialtyChoices(models.TextChoices):
        MAMMAL = "Mammals"
        BIRDS = "Birds"
        REPTILES = "Reptiles"
        OTHERS = "Others"

    specialty = models.CharField(max_length=10, choices=SpecialtyChoices.choices)
    managed_animals = models.ManyToManyField("Animal")

    # 04 Add custom Validation
    def clean(self):
        super().clean()
        choices_dynamic = self.SpecialtyChoices.values
        if self.specialty not in choices_dynamic:
            raise ValidationError("Specialty must be a valid choice.")


# 07 Custom BooleanChoice Field
class BooleanChoiceField(models.BooleanField):
    
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = (
            (True, "Available"),
            (False, "Not Available")
        )
        kwargs["default"] = True
        
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()


    def is_available(self):
        return self.availability


#03
class ZooDisplayAnimal(Animal):

    class Meta:
        proxy = True

    # 05 Animal Display System
    def __extra_info(self):
        extra_info = str()

        if hasattr(self, "mammal"):
            extra_info = f" Its fur color is {self.mammal.fur_color}."

        elif hasattr(self, "bird"):
            extra_info = f" Its wingspan is {self.bird.wing_span} cm."

        elif hasattr(self, "reptile"):
            extra_info = f" Its scale type is {self.reptile.scale_type}."

        return extra_info


    def display_info(self):
        info = (f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}. "
                f"It makes a noise like '{self.sound}'!{self.__extra_info()}")

        return info

    def is_endangered(self):
        return self.species in ["Cross River Gorilla", "Orangutan", "Green Turtle"]



