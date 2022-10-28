from django.contrib import admin
from .models import Shipment, Order

admin.site.register(Order)
admin.site.register(Shipment)
