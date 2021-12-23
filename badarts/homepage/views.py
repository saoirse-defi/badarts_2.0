from django.shortcuts import render, redirect, reverse
from .models import Message
from .forms import MessageForm


def index(request):
    template = 'homepage/index.html'

    context = {

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
