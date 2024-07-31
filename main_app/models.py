from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    date_time = models.DateTimeField('Date & Time')
    room_area = models.CharField(max_length=100)
    attendees = models.IntegerField()
    performances = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.id})

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('venue-detail', kwargs={'venue_id': self.id})
    
