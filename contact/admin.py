from django.contrib import admin
from django.utils.html import format_html 
#
from contact.models import Message, Contactcontent


@admin.register(Contactcontent)
class Contactcontent(admin.ModelAdmin): 
    def has_add_permission(self, request): 
        return False 


@admin.register(Message) 
class MessageAdmin(admin.ModelAdmin): 


    list_display = ['message_from', 'sent_on', 'is_read']
    readonly_fields = ['sent_on', 'email', 'message']
    list_editable = ['is_read']

    def message_from(self, obj): 
        return format_html(f'{obj.email}  (click here to read)')
        
    def has_add_permission(self, request):
        return False

