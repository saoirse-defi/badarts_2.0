from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import MessageForm
from .models import Artist, Release, Event, Message


def index(request):
    artists = Artist.objects.all()
    releases = Release.objects.all()
    events = Event.objects.all()
    messages = Message.objects.all()

    template = 'homepage/index.html'
    context = {
        'artists': artists,
        'releases': releases,
        'events': events,
        'messages': messages
    }

    return render(request, template, context)


def contact(request):

    template = 'homepage/contact.html'
    context = {
    }

    return render(request, template, context)


def events(request):
    event_list = Event.objects.all()

    template = 'homepage/events.html'
    context = {
        'event_list': event_list,
    }

    return render(request, template, context)


def event_page(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    template = 'homepage/event_page.html'
    context = {
        'event': event,
    }

    return render(request, template, context)


def artist_profile(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    template = 'homepage/artist_profile.html'
    context = {
        'artist': artist,
    }

    return render(request, template, context)


def recording(request):

    template = 'homepage/recording.html'
    context = {}

    return render(request, template, context)
