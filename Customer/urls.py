from django.urls import path
from . import views


urlpatterns = [
    path('home',views.home),
    path('logout',views.logout),
    path('Logout',views.Logout),
    path('contact',views.contact),
    path('roomservice',views.roomservice),
    path('luggageservice',views.luggageservice),
]