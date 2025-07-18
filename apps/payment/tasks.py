from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_status_email(user_email, booking_id, status_display, user_id=None):
    send_mail(
        subject=f'Изменение статуса брони #{booking_id}',
        message=f'Ваш статус бронирования изменён на: {status_display}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=True,
    )
