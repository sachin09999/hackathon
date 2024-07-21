from django.db import models

# Create your models here.

class contactEnquiry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='static/contact_enquiry_photos/')

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    photo = models.ImageField(upload_to='event_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()

    def __str__(self):
        return self.name

    
   
