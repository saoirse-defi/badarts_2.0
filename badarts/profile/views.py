from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

from django.contrib.auth.models import User


@login_required()
def my_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.all().filter(user_profile=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect(reverse('my_profile'))
        else:
            messages.error(request, 'Please review profile details as '
                           'there appears to be an error.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profile/my_profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)

