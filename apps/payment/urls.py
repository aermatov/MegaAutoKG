from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payment.views import BookingViewSet, PaymentStatusViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'payment-statuses', PaymentStatusViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
