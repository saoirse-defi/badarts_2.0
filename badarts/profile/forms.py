from django import forms
from django.contrib.auth import (
    get_user_model
)

from .models import UserProfile, County
from localflavor.ie.forms import EircodeField


User = get_user_model()