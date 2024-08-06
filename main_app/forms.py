from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'producer', 'date_time', 'room_area', 'attendees', 'performances']
        widgets = {
            'date_time': forms.DateTimeInput(
                format=('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
            )
        }
