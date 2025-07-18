# Generated by Django 5.2.4 on 2025-07-10 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_options_alter_carbrand_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='carbrand',
            options={'verbose_name': 'Марка автомобиля', 'verbose_name_plural': 'Марки автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='carbrandtype',
            options={'verbose_name': 'Марка и тип автомобиля', 'verbose_name_plural': 'Марка и тип автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='cartype',
            options={'verbose_name': 'Тип автомобиля', 'verbose_name_plural': 'Типы автомобилей'},
        ),
        migrations.AlterModelOptions(
            name='drivetype',
            options={'verbose_name': 'Тип привода', 'verbose_name_plural': 'Типы привода'},
        ),
        migrations.AlterModelOptions(
            name='fueltype',
            options={'verbose_name': 'Тип топлива', 'verbose_name_plural': 'Типы топлива'},
        ),
        migrations.AlterModelOptions(
            name='gearboxtype',
            options={'verbose_name': 'Коробка передачи', 'verbose_name_plural': 'Коробки передач'},
        ),
    ]
