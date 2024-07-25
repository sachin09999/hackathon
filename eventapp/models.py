from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# class contactEnquiry(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=300)
#     photo = models.ImageField(upload_to='static/contact_enquiry_photos/')

#     def __str__(self):
#         return self.name
    
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
    photo = models.ImageField(upload_to='event_photos/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='comedy')
    location = models.CharField(max_length=200,default='Unknown Location')

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    room = models.CharField(max_length=255)
    sender = models.CharField(max_length=10)  # 'client' or 'admin'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} ({self.timestamp}): {self.message[:20]}"    

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.event.name}'    