from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from generics.models import TitleInfo, DateTimeInfo


User = get_user_model()


class CarBrand(TitleInfo):
    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class CarType(TitleInfo):
    class Meta:
        verbose_name = 'Тип автомобиля'
        verbose_name_plural = 'Типы автомобилей'


class CarBrandType(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_brand')
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, related_name='car_type')

    class Meta:
        unique_together = ('car_brand', 'car_type')
        verbose_name = 'Марка и тип автомобиля'
        verbose_name_plural = 'Марка и тип автомобилей'

    def __str__(self):
        return f'{self.car_brand.title} - {self.car_type.title}'


class GearboxType(TitleInfo):
    class Meta:
        verbose_name = 'Коробка передачи'
        verbose_name_plural = 'Коробки передач'


class DriveType(TitleInfo):
    class Meta:
        verbose_name = 'Тип привода'
        verbose_name_plural = 'Типы привода'


class FuelType(TitleInfo):
    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'


class Car(DateTimeInfo):
    WHEEL_CHOICES = [('left', 'Левый руль'), ('right', 'Правый руль')]
    model = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars/')
    price = models.CharField(max_length=30)
    consumption = models.CharField(max_length=30)
    year_publication = models.PositiveSmallIntegerField( validators=[MinValueValidator(1886), MaxValueValidator(2100)])
    wheel = models.CharField(max_length=10, choices=WHEEL_CHOICES, default='left')
    description = models.TextField()
    gearbox_type = models.ForeignKey(GearboxType, on_delete=models.SET_NULL, null=True)
    drive_type = models.ForeignKey(DriveType, on_delete=models.SET_NULL, null=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True)
    car_brand_type = models.ForeignKey(CarBrandType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.model


class CarStatusHistory(models.Model):
    STATUS_CHOICES = (
        ('available', 'Доступный'),
        ('booked', 'Забронирован'),
        ('maintenance', 'На ремонте'),
        ('unavailable', 'Недоступный'),
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'История статуса'
        verbose_name_plural = 'Истории статусов'

    def __str__(self):
        return f"{self.car} — {self.status} ({self.changed_at:%Y-%m-%d})"
