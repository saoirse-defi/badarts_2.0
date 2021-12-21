from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_name = models.CharField(max_length=80, null=True, blank=True)
    phone_number = models.CharField(max_length=20,
                                    null=True, blank=True)
    street_address1 = models.CharField(max_length=80,
                                       null=True, blank=True)
    street_address2 = models.CharField(max_length=80,
                                       null=True, blank=True)
    town = models.CharField(max_length=40,
                            null=True, blank=True)
    county = models.ForeignKey('County',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    country = CountryField(blank_label='Country',
                           null=True, blank=True)
    postcode = models.CharField(max_length=20,
                                null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class County(models.Model):
    verbose_name_plural = 'Counties'

    name = models.CharField(max_length=254, blank=False)

    def __str__(self):
        return str(self.name)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
