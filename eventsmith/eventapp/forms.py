from django import forms

from .models import contactEnquiry,Event

class Event(forms.ModelForm):
    class Meta:
        model = contactEnquiry
        fields = ['name', 'start_date', 'description', 'photo', 'price', 'category', 'location']

       