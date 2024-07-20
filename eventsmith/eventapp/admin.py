
from django.contrib import admin

from .models import RSVP, Event

# Register your models here.
admin.site.register(Event)
admin.site.register(RSVP)