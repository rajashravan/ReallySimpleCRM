from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url="/login/")
def index(request):
    return HttpResponseRedirect(reverse('contacts:index'))
