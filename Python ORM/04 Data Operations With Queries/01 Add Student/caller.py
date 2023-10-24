import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():
    student_data = [
        {
            "student_id": "FC5204",
            "first_name": "John",
            "last_name": "Doe",
            "birth_date": "1995-05-15",
            "email": "john.doe@university.com",
        },
        {
            "student_id": "FE0054",
            "first_name": "Jane",
            "last_name": "Smith",
            "birth_date": None,
            "email": "jane.smith@university.com",
        },
        {
            "student_id": "FH2014",
            "first_name": "Alice",
            "last_name": "Johnson",
            "birth_date": "1998-02-10",
            "email": "alice.johnson@university.com",
        },
        {
            "student_id": "FH2015",
            "first_name": "Bob",
            "last_name": "Wilson",
            "birth_date": "1996-11-25",
            "email": "bob.wilson@university.com",
        },
    ]

    for data in student_data:

        student = Student(
            student_id=data["student_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=data["birth_date"],
            email=data["email"],
        )
        student.save()



add_students()



# Import your models
# Create and check models
# Run and print your queries

