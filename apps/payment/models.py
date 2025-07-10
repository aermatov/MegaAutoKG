from django.contrib.auth import get_user_model
from django.db import models
from apps.car.models import Car
from generics.models import TitleInfo


User = get_user_model()


class Booking(models.Model):
    start_time = models.DateTimeField()
    end_time =  models.DateTimeField()
    total_cost = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f'Booking #{self.id} by {self.user}'


class PaymentStatus(TitleInfo):
    class Meta:
        verbose_name = 'История брони'
        verbose_name_plural = 'Истории брони'


class Payment(models.Model):
    amount = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        return f'Payment #{self.id} - {self.amount}'
