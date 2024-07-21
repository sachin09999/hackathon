from django import forms

from .models import contactEnquiry

class contactEnquiryForm(forms.ModelForm):
    class Meta:
        model = contactEnquiry
        fields = ['name', 'description', 'date', 'time', 'location', 'photo']

       