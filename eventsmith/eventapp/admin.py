
from django.contrib import admin
from .models import ChatMessage
from django.urls import path
from .views import admin_chat

# Register your models here.

from .models import contactEnquiry
from .models import Event

@admin.register(contactEnquiry)
class contactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location')
    search_fields = ('name', 'location')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'price')
    search_fields = ('name',)

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sender', 'message', 'timestamp')
    list_filter = ('room', 'sender')
    search_fields = ('message',)

admin.site.register(ChatMessage, ChatMessageAdmin)    
class MyAdminSite(admin.AdminSite):
    site_header = 'My Admin Dashboard'
    site_title = 'Admin'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin_chat/', self.admin_view(admin_chat), name='admin_chat'),
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='myadmin')