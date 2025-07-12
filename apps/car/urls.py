from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    CarViewSet, CarBrandViewSet, CarTypeViewSet,
    CarBrandTypeViewSet, GearboxTypeViewSet, DriveTypeViewSet,
    FuelTypeViewSet, CarStatusHistoryViewSet
)

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'car-brands', CarBrandViewSet)
router.register(r'car-types', CarTypeViewSet)
router.register(r'car-brand-types', CarBrandTypeViewSet)
router.register(r'gearbox-types', GearboxTypeViewSet)
router.register(r'drive-types', DriveTypeViewSet)
router.register(r'fuel-types', FuelTypeViewSet)
router.register(r'car-status-history', CarStatusHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
