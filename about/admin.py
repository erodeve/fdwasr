from django.contrib import admin
#
from about.models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin): 
    def has_add_permission(self, request):
        return False


