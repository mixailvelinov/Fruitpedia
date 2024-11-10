from django.core.validators import MinLengthValidator
from django.db import models
from profiles.validators import first_letter_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            first_letter_validator,
        ]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            first_letter_validator,
        ]
    )

    email = models.EmailField(max_length=40)

    password = models.CharField(
        help_text='*Password length requirements: 8 to 20 characters',
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ]
    )

    image = models.URLField(blank=True, null=True)

    age = models.IntegerField(null=True, blank=True, default=18)