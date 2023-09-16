from django import forms
from django.contrib.auth import get_user_model

from contact.models import Message

# User = get_user_model()


class ContactForm(forms.Form):
    # class Meta:
    #     model = Message  # Specify the model that this form is based on
    #     fields = ['user', 'email', 'content']
    user = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'user'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'content'
        }
    ))

    # def clean_user(self):
    #     user = self.cleaned_data.get('user')
    #     foo = User.objects.filter(user=user)
    #     if foo.exists():
    #         raise forms.ValidationError('Username is already taken')
    #     return user
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     foo = User.objects.filter(email=email)
    #     if foo.exists():
    #         raise forms.ValidationError('Email is already taken')
    #     return email
    #
    # def clean(self):
    #     data = self.cleaned_data
    #     email = data.get('email')
    #     user = data.get('user')
    #     content = data.get('content')
    #     if len(content) < 4:
    #         raise forms.ValidationError('Content must be greater than 4 characters long')
    #     return data
    #
    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(ContactForm, self).save(commit=False)
    #     # user.active = False # send confirmation email
    #     if commit:
    #         user.save()
    #     return user
    #

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'user',
            'email',
            'content'
        ]
