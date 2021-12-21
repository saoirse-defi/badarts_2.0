from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def my_profile(request):
    template = 'profile/my_profile.html'

    context = {

    }

    return render(request, template, context)


def login(request):
    template = 'profile/login.html'

    context = {

    }

    return render(request, template, context)


def signup(request):
    template = 'profile/signup.html'

    context = {

    }

    return render(request, template, context)
