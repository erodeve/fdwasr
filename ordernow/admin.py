from django.contrib import admin
from ordernow.models import Order 


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ['order_date', 'is_delivered']
    