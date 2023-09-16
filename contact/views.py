from django.contrib.auth import get_user_model
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from .models import *
from .mixins import *
from django.forms.utils import ErrorList
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

User = get_user_model()
# Create your views here.


class MessageListView(ListView):
    queryset = Message.objects.all()
    template_name = 'list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = Message.objects.all()
        print(self.request.GET)
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
            # qs = qs.filter(Q(content__icontains=query) | Q(user__username__icontains=query)) #If gusto na exact (content__iexact=query)
        return qs


class MessageDetailView(DetailView):
    queryset = Message.objects.all()
    template_name = 'detail_view.html'

    def get_object(self, queryset=Message.objects.all()):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        return Message.objects.get(id=pk)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        user = contact_form.cleaned_data.get('user')
        email = contact_form.cleaned_data.get('email')
        content = contact_form.cleaned_data.get('content')
        # new_user = Message.objects.create_user(user, email, content)

    return render(request, 'contact_page.html', context)

# views.py

# from django.views.generic import ListView
# from .models import Message
# from .mixins import AdminRequiredMixin
#
# class ContactMessageListView(AdminRequiredMixin, ListView):
#     model = Message
#     template_name = 'list_view.html'
#     context_object_name = 'messages'
#
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Optionally, you can send an email to the website owner here.
#     else:
#         form = ContactForm()
#
#     messages = Message.objects.all()
#     return render(request, 'contact_page.html', {'form': form, 'messages': messages})
