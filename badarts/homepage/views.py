from django.shortcuts import render, redirect, reverse
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
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact'))
    else:
        form = MessageForm()

    template = 'homepage/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
