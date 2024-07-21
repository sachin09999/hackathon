
from django.contrib import admin




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