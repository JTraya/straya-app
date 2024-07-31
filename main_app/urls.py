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
]