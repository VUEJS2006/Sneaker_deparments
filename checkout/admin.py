from django.contrib import admin
from . models import Order, OrderItem, Profile
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
