# Generated by Django 5.1.2 on 2024-10-26 12:42

import django.core.validators
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_mame', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), profiles.validators.first_letter_validator])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), profiles.validators.first_letter_validator])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(help_text='*Password length requirements: 8 to 20 characters', max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image', models.URLField(blank=True, null=True)),
                ('aage', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
