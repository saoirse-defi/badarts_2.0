from django.contrib import admin
from .models import Message, Release, Artist, Event, Photo

# Register your models here.
admin.site.register(Message)
admin.site.register(Release)
admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Photo)
