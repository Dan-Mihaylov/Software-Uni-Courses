from django.core.exceptions import ValidationError


def validate_space_in_name(value):
    if " " in value:
        raise ValidationError('Space Now Allowed In First Name')