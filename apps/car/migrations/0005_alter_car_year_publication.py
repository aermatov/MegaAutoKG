# Generated by Django 5.2.4 on 2025-07-10 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_alter_car_options_alter_carbrand_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year_publication',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1886), django.core.validators.MaxValueValidator(2100)]),
        ),
    ]
