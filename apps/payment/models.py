from django.contrib.auth import get_user_model
from django.db import models
from apps.car.models import Car
from generics.models import TitleInfo, DateTimeInfo
from apps.payment.tasks import send_booking_status_email


User = get_user_model()


class Booking(DateTimeInfo):
    STATUS_CHOICES = [
        ('processing', 'В обработке'),
        ('sent', 'Отправлен'),
        ('delivered', 'Завершён'),
        ('cancelled', 'Отменён'),
    ]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return f'Booking #{self.id} by {self.user}'

    def save(self, *args, **kwargs):
        if self.pk:
            old_status = Booking.objects.get(pk=self.pk).status
            if old_status != self.status:
                send_booking_status_email.delay(
                    self.user.email,
                    self.id,
                    self.get_status_display()
                )
        super().save(*args, **kwargs)


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
