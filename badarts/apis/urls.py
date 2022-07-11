from django.urls import include, path
from rest_framework import routers
from .views import api_artist_view

#from .views import ArtistAPIViewset

#router = routers.DefaultRouter()

#router.register(r'artists/', api_artist_view, basename='Artist')

urlpatterns = [
    path('', api_artist_view, name='artistAPI'),
    path('api-auth/', include('rest_framework.urls')),
]
