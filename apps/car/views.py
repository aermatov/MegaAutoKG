import logging

from rest_framework import viewsets, filters
from .models import (
    Car, CarBrand, CarType, CarBrandType,
    GearboxType, DriveType, FuelType, CarStatusHistory
)
from .serializers import (
    CarSerializer, CarBrandSerializer, CarTypeSerializer,
    CarBrandTypeSerializer, GearboxTypeSerializer, DriveTypeSerializer,
    FuelTypeSerializer, CarStatusHistorySerializer
)
from .filters import CarFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAdminOrReadOnly, IsAdminANDLAdminOrReadOnly


logger = logging.getLogger(__name__)


class CarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminANDLAdminOrReadOnly]
    queryset = Car.objects.all().order_by('-year_publication')
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CarFilter
    search_fields = ['model', 'description']


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarTypeViewSet(viewsets.ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class CarBrandTypeViewSet(viewsets.ModelViewSet):
    queryset = CarBrandType.objects.all()
    serializer_class = CarBrandTypeSerializer


class GearboxTypeViewSet(viewsets.ModelViewSet):
    queryset = GearboxType.objects.all()
    serializer_class = GearboxTypeSerializer


class DriveTypeViewSet(viewsets.ModelViewSet):
    queryset = DriveType.objects.all()
    serializer_class = DriveTypeSerializer


class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class CarStatusHistoryViewSet(viewsets.ModelViewSet):
    queryset = CarStatusHistory.objects.all().order_by('-changed_at')
    serializer_class = CarStatusHistorySerializer
