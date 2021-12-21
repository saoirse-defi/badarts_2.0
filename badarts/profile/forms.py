from django import forms
from django.contrib.auth import (
    get_user_model
)

from .models import UserProfile, County
from localflavor.ie.forms import EircodeField


User = get_user_model()


class UserProfileForm(forms.ModelForm):
    """ Creates and validates UserProfile form."""
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Adds placeholders and classes,
            remove auto-gen labels and sets
            autofocus on first field."""

        super().__init__(*args, **kwargs)

        self.fields['default_county'] = forms.ModelChoiceField(
                                        queryset=County.objects.order_by('name'),
                                        initial=0)
        self.fields['default_postcode'] = EircodeField()