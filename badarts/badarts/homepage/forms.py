from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """ Creates and validates Message form."""
    class Meta:
        model = Message
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        """Adds placeholders and classes,
            remove auto-gen labels and sets
            autofocus on first field."""

        super().__init__(*args, **kwargs)
