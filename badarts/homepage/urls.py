from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('<uuid:artist_id>', views.artist_profile, name='artist_profile'),
]
