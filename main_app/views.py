from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Venue, Event
# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

class VenueCreate(CreateView):
    model = Venue
    fields = ['name', 'location', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VenueUpdate(UpdateView):
    model = Venue
    fields = ['name', 'location', 'description']

class VenueDelete(DeleteView):
    model = Venue
    success_url = '/venues/'

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'producer', 'date_time', 'room_area', 'attendees', 'performances']

class EventList(ListView):
    model = Event

class EventDetail(DetailView):
    model = Event

class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'producer', 'date_time', 'room_area', 'attendees', 'performances']

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/'


def about(request):
    return render(request, 'about.html')



def venue_index(request):
    venues = Venue.objects.all()
    return render(request, 'venues/index.html', {'venues': venues})

def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    events_not_in_venue = Event.objects.exclude(id__in = venue.events.all().values_list('id'))
    return render(request, 'venues/venue_details.html', {'venue': venue, 'events': events_not_in_venue})

def associate_event(request, venue_id, event_id):
    Venue.objects.get(id=venue_id).events.add(event_id)
    return redirect('venue-detail', venue_id=venue_id)

def remove_event(request, venue_id, event_id):
    Venue.objects.get(id=venue_id).events.remove(event_id)
    return redirect('venue-detail', venue_id=venue_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('venue-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)