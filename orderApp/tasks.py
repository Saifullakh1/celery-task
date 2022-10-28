from celery import shared_task
from celery.loaders import app
from orderSystem.celery import app
from django.core.mail import EmailMessage
from django.core.mail import send_mail


@shared_task
def send_message_to_email(email):
    send_mail(
        f'Hello {email}, I am ГАИ',
        "You must pay 1000$ for my Steam Account, if you don't pay I'm gonna kill you",
        'nursultandev@gmail.com',
        [email],
        fail_silently=False,
    )


@shared_task
def send_shipment_email(owner_name, order_name, owner_email):
    send_mail(
        f'Hello {owner_name}',
        f"Your order {order_name} is ready to be shipped\n Kindly have patience.\n regards.",
        'saifullakh7@gmail.com',
        [owner_email],
        fail_silently=False,
    )

    # mail_subject = "Your order is ready"
    # message = "Hello {0}, your order {1} is ready to be shipped\n Kindly have patience.\n regards.".format(
    #     owner_name, order_name
    # )
    # email = EmailMessage(mail_subject, message, to=[owner_email])
    # email.send()

# @shared_task
# def send_message(owner_name, order_name, owner_email):
