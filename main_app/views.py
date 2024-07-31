from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello from Straya!<h1>')

def about(request):
    return render(request, 'about.html')


class Venue:
    def __init__(self, name, location, description, User):
        self.name = name
        self.location = location
        self.description = description
        self.User = User

venues  = [
    Venue('Powerhouse', '1347 Folsom St', 'Dive Bar', 'Dakota'),
    Venue('Oasis', '298 Eleventh St', 'Nightclub and Performance venue', 'Darcy'),
]


def venue_index(request):
    return render(request, 'venues/index.html', {'venues': venues})


class Event:
    def __init__(self, name, producer, time, room_area, number_of_people, perfrmances, venue, User):
        self.name = name
        self.producer = producer
        self.time = time
        self.room_area = room_area
        self.number_of_people = number_of_people
        self.performances = perfrmances
        self.venue = venue
        self.User = User

def event_index(request):
    return render(request, 'events/index.html', {'events': events})