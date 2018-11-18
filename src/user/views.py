from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import Register

# Create your views here.


def register(request):
    form = Register(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'You created a user: {username}!')
        return redirect('home')

    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'wxservice/profile.html')
