from celery import shared_task
from time import sleep

@shared_task
def send_welcome_email(email):
    sleep(5)
    print(f"Sent welcome email to {email}")
    return True
