from django.contrib import admin

from apps.payment.models import Booking, PaymentStatus, Payment


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time', 'total_cost', 'user', 'car']


admin.site.register(Booking, BookingAdmin)


class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(PaymentStatus, PaymentStatusAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'timestamp', 'booking', 'payment_status', 'user']


admin.site.register(Payment, PaymentAdmin)
