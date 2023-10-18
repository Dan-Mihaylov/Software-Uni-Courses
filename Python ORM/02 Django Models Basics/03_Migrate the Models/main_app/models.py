from django.db import models

CHOICES = [
    ('Sofia', 'Sofia'),
    ('Plovdiv', 'Plovdiv'),
    ('Burgas', 'Burgas'),
    ('Varna', 'Varna')
]


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email_address}"


class Department(models.Model):
    code = models.CharField(primary_key=True, max_length=4, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField("Employees Count", default=1)
    location = models.CharField(max_length=20, blank=True, choices=CHOICES)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.code}, {self.name}"
