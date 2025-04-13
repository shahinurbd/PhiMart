from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size = 10
    max_size_in_byte = max_size * 1024 * 1024

    if file.size > max_size_in_byte:
        raise ValidationError(f"File can not be larger than {max_size}MB")

