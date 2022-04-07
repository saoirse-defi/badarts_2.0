import uuid
from django.db import models


class Artist(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=254)
    bio = models.TextField(max_length=4096, default="")
    youtube_url = models.URLField(max_length=1024, null=True, blank=True)
    instagram_url = models.URLField(max_length=1024, null=True, blank=True)
    spotify_url = models.URLField(max_length=1024, null=True, blank=True)
    bandcamp_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)


class Release(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=254)
    artist = models.ForeignKey(Artist,
                               null=True,
                               blank=False,
                               default=None,
                               on_delete=models.CASCADE)
    recorded_by = models.CharField(max_length=254)
    youtube_url = models.URLField(max_length=1024, null=True, blank=True)
    spotify_url = models.URLField(max_length=1024, null=True, blank=True)
    bandcamp_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True, null=False, blank=False)
    carousel_active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.title)


class Event(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=254)
    venue = models.CharField(max_length=254)
    date = models.DateField()
    time = models.TimeField()
    eventbrite_url = models.URLField(max_length=1024, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    artists = models.ManyToManyField(Artist)
    expired = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return str(self.name)

    def display_performer_names(self):
        return ', '.join([performer.name for performer in self.artists.all()])


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
