from django.contrib import admin
from .models import *
from .forms import MessageModelForm
from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.
class MessageModelAdmin(admin.ModelAdmin):
    form = MessageModelForm


# User = get_user_model()

admin.site.register(Message, MessageModelAdmin)
# admin.site.register(User)
