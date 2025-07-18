# Generated by Django 5.2.4 on 2025-07-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_booking_options_alter_payment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('processing', 'В обработке'), ('sent', 'Отправлен'), ('delivered', 'Завершён'), ('cancelled', 'Отменён')], default='processing', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
