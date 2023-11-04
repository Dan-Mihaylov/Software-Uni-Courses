import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import (
    Animal, Mammal, Bird, Reptile, Employee, ZooKeeper, Veterinarian, ZooDisplayAnimal
)
from datetime import date, timedelta


