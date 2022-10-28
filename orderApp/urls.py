from django.urls import path

from .views import CreateOrder, CreateShipment, send_email

urlpatterns = [
    path("orders", CreateOrder.as_view()),
    path("shipments", CreateShipment.as_view()),
    path('send', send_email, name='send')
]


