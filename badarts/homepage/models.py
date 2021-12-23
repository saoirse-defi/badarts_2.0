import uuid
from django.db import models


class Release(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    artist2 = models.CharField(max_length=254)
    artist3 = models.CharField(max_length=254)
    producer = models.CharField(max_length=254)
    recorded_by = models.CharField(max_length=254)
    youtube_url = models.URLField(max_length=1024, null=True, blank=True)
    spotify_url = models.URLField(max_length=1024, null=True, blank=True)
    bandcamp_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.title)


class Message(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=254)

    def __str__(self):
        return str(self.subject)
