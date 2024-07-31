from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('venue-detail', kwargs={'venue_id': self.id})