
from django.contrib import admin
from .models import ChatMessage
from django.urls import path
from .views import admin_chat
from .models import UserProfile


# Register your models here.

from .models import Event

# @admin.register(contactEnquiry)
# class contactEnquiryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date', 'time', 'location')
#     search_fields = ('name', 'location')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','photo','category','location')
    search_fields = ('name','location')

 

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


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_events']

    def get_events(self, obj):
        return ", ".join([event.name for event in obj.events.all()])

    get_events.short_description = 'Events Joined'

admin.site.register(UserProfile, UserProfileAdmin)