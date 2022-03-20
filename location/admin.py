from django.contrib import admin
# 
from location.models import Location  


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin): 
    def has_add_permission(self, request) -> bool:
        return False
        