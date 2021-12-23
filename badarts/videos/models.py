import uuid
from django.db import models


class Video(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=254)
    thumbnail_url = models.CharField(max_length=254)
    youtube_url = models.CharField(max_length=254)
    data_caption = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    active = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)
