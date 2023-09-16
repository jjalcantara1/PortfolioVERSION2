from django.shortcuts import render, redirect
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Message


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def projects(request):
    return render(request, 'projects.html', {})


