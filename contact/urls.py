from django.contrib import admin
from django.urls import path, include, re_path  # para mainclude ung views ng tweets app
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from templates import *
from .models import *
app_name = 'contact'

urlpatterns = [
    path('', MessageListView.as_view(), name='list-view'),
    re_path(r'^(?P<pk>\d+)/$', MessageDetailView.as_view(), name='detail-view'),
]
