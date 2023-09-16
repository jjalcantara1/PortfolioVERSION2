from django.conf import settings
from django.db import models
from django.urls import reverse_lazy


# Create your models here.
# models.Model - required to; inherit


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=280)
    content = models.CharField(max_length=280)
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    # lagay sa loob ng () ung limit ng no of characters

    def __str__(self):
        return str(self.content)
    # dapat nakaindent sa loob ng class

    def get_absolute_url(self):
        return reverse_lazy('contact:detail-view', kwargs={'pk': self.pk})
