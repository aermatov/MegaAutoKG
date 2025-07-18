from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.payment.models import Booking, PaymentStatus, Payment
from apps.payment.serializers import BookingSerializer, PaymentStatusSerializer, PaymentSerializer
from apps.payment.permissions import IsOwnerOrAdmin


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentStatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = PaymentStatus.objects.all()
    serializer_class = PaymentStatusSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

