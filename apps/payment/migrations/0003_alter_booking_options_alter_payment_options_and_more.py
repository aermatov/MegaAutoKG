# Generated by Django 5.2.4 on 2025-07-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Брони'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Оплата', 'verbose_name_plural': 'Оплаты'},
        ),
        migrations.AlterModelOptions(
            name='paymentstatus',
            options={'verbose_name': 'История брони', 'verbose_name_plural': 'Истории брони'},
        ),
    ]
