from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm

UserModel = get_user_model()


class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2']


