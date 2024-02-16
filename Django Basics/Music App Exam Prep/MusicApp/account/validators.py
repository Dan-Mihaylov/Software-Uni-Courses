from django.core.exceptions import ValidationError


def username_char_validator(value: str):
    if all([x.isalnum() or x == '_' for x in value]):
        return value
    else:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
