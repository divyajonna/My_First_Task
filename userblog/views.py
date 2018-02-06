# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import UserPost
from django.utils import timezone

#this is to create postdetail
from django.shortcuts import render, get_object_or_404

#to create postform
from .forms import PostForm

#to create custom permissions
from django.contrib.auth.decorators import permission_required

from django.http import HttpResponseForbidden

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #removed the below line as it showing 2-arg cant be taken error
            #login(request,user)
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
#@permission_required('UserPost.itposts', raise_exception =True)
def userpost_list(request):
        #u.user_permissions.add(user_permisssions.get(permissions))
        posts=UserPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'userblog/userpost_list.html',{'posts':posts})



#to view our published postdetails
@login_required
def userpost_detail(request, pk):
    post = get_object_or_404(UserPost, pk=pk)
    return render(request, 'userblog/userpost_detail.html', {'post': post})

#this is to postnew and to save the form
@login_required
def userpost_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('userpost_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'userblog/userpost_edit.html', {'form': form})

#this is to enable editing of the forms
@login_required
def userpost_edit(request, pk):
    post = get_object_or_404(UserPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #both when we save the form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('userpost_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) #when we've just opened a form with this post to edit:
    return render(request, 'userblog/userpost_edit.html', {'form': form})
