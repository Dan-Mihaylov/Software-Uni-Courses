from django import forms

from .models import Pet


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'photo']



