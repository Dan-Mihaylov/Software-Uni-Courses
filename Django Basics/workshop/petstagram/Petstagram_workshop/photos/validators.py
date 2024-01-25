from django.core.exceptions import ValidationError


MAX_FILE_SIZE = 5242880


def validate_file_size(file):

    if file.size > MAX_FILE_SIZE:
        raise ValidationError(f'The maximum file size can be {MAX_FILE_SIZE}')
