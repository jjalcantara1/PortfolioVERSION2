from django.shortcuts import render
from django.views.generic import CreateView

from contact.forms import ContactForm


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def projects(request):
    return render(request, 'projects.html', {})


def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact_page.html', context)
