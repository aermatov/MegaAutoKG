from celery import shared_task

from generics.utils import send_message


@shared_task
def send_message_register(email, id):
    send_message(email, id)