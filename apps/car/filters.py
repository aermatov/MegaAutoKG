from django_filters import rest_framework as filters
from .models import Car


class CarFilter(filters.FilterSet):
    model = filters.CharFilter(field_name='model', lookup_expr='icontains')
    year_publication = filters.RangeFilter()
    price = filters.CharFilter(lookup_expr='icontains')
    car_brand = filters.CharFilter(
        field_name='car_brand_type__car_brand__title', lookup_expr='icontains'
    )
    car_type = filters.CharFilter(
        field_name='car_brand_type__car_type__title', lookup_expr='icontains'
    )

    class Meta:
        model = Car
        fields = [
            'model',
            'car_brand',
            'car_type',
            'gearbox_type',
            'drive_type',
            'fuel_type',
            'wheel',
            'year_publication',
            'price',
        ]
