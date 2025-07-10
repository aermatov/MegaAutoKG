from django.contrib import admin

from apps.car.models import (
    CarBrand,
    CarType,
    CarBrandType,
    GearboxType,
    DriveType,
    FuelType,
    Car,
    CarStatusHistory
)


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(CarBrand, CarBrandAdmin)


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(CarType, CarTypeAdmin)


class CarBrandTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'car_brand', 'car_type']


admin.site.register(CarBrandType, CarBrandTypeAdmin)


class GearboxTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(GearboxType, GearboxTypeAdmin)


class DriveTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(DriveType, DriveTypeAdmin)


class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(FuelType, FuelTypeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'image',
        'price',
        'consumption',
        'year_publication',
        'wheel',
        'description',
        'gearbox_type',
        'drive_type',
        'fuel_type',
        'car_brand_type',
    ]


admin.site.register(Car, CarAdmin)


class CarStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'car', 'status', 'changed_at', 'changed_by']


admin.site.register(CarStatusHistory, CarStatusHistoryAdmin)
