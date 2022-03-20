from django.contrib import admin
#
from menu.models import Menu 


@admin.register(Menu) 
class MenuAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price')
    list_editable = ['price']

