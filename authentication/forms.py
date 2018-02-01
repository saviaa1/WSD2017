from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required! Type in your email address')
    #developer = forms.BooleanField(help_text='Tick box if you are a developer', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',) # 'developer',
