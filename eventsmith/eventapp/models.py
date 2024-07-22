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
    CATEGORY_CHOICES = [
        ('comedy', 'Comedy Shows'),
        ('workshops', 'Workshops'),
        ('meetups', 'Meetups'),
        ('music', 'Music Shows'),
        ('kids', 'Kids'),
        ('exhibitions', 'Exhibitions'),
        ('performances', 'Performances'),
    ]
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    description = models.TextField(default='No description available')
    photo = models.ImageField(upload_to='event_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='comedy')

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    room = models.CharField(max_length=255)
    sender = models.CharField(max_length=10)  # 'client' or 'admin'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} ({self.timestamp}): {self.message[:20]}"    

    
   
