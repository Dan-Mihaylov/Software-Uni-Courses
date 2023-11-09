from django.core.exceptions import ValidationError


def customer_name_validator(value: str):
    if not value.replace(" ", "").isalpha():
        raise ValidationError("Name can only contain letters and spaces")


# Be careful of multiple True/False Conditions
def phone_number_validator(value: str):
    if not value.startswith("+359") or len(value) != 13 or not all([char.isdigit() for char in value[4:]]):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


def min_age_validator(value: int):
    if value < 18:
        raise ValidationError("Age must be greater than 18")

