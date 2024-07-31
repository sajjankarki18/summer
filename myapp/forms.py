from typing import Any
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter your email'})
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter your username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder': 'confirm password'})
        