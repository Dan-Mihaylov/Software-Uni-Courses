from django import forms
from .models import Profile


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'name': 'username',
                'type': 'text',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'name': 'email',
                'type': 'email',
                'placeholder': 'Email',
            }),
            'age': forms.NumberInput(attrs={
                'id': 'age',
                'name': 'age',
                'type': 'number',
                'min': '0',
                'placeholder': 'Age',
            }),
        }
