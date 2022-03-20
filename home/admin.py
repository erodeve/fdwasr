from django.contrib import admin
from home.models import Homecontent, Mapboxtoken


@admin.register(Mapboxtoken) 
class Mapboxtoken(admin.ModelAdmin): 
    def has_add_permission(self, request) -> bool:
        return False 


@admin.register(Homecontent)
class Homecontent(admin.ModelAdmin): 
    def has_add_permission(self, request) -> bool:
        return False 

