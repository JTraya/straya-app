from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('venues/', views.venue_index, name='venue-index'),
    path('venues/<int:venue_id>/', views.venue_detail, name='venue-detail'),
    path('venues/create/', views.VenueCreate.as_view(), name='venue-create'),
    path('venues/<int:pk>/update/', views.VenueUpdate.as_view(), name='venue-update'),
    path('venues/<int:pk>/delete/', views.VenueDelete.as_view(), name='venue-delete'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('events/', views.EventList.as_view(), name='event-index'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('venues/<int:venue_id>/associate-event/<int:event_id>/', views.associate_event, name='associate-event'),
]