from rest_framework import serializers
from .models import CarBrand, CarType, CarBrandType, GearboxType, DriveType, FuelType, CarStatusHistory, Car


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = '__all__'


class CarBrandTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrandType
        fields = '__all__'


class GearboxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearboxType
        fields = '__all__'


class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveType
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    gearbox_type = GearboxTypeSerializer()
    drive_type = DriveTypeSerializer()
    fuel_type = FuelTypeSerializer()
    car_brand_type = CarBrandTypeSerializer()

    class Meta:
        model = Car
        fields = '__all__'


class CarStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatusHistory
        fields = '__all__'
