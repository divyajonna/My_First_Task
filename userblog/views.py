# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import UserPost
from django.utils import timezone

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'userblog/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'userblog/home.html')

def login(request):
    return render(request, 'userblog/login.html')

@login_required
def userpost_list(request):
    posts=UserPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'userblog/userpost_list.html',{'posts':posts})
