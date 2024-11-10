from django.core.validators import MinLengthValidator
from django.db import models
from fruits.validators import fruit_name_validator
from profiles.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            fruit_name_validator,
        ],
        error_messages={
            'unique': 'This fruit name is already in use! Try a new one.'
        }
    )

    image = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

