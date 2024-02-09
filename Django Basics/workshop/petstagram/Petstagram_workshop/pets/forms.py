from django import forms

from .models import Pet
from ..mixins.form_mixins import ReadOnlyFieldFormMixin


class PetForm(forms.ModelForm, ReadOnlyFieldFormMixin):
    """ This is a base form for creating, editing and deleting Pets. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Pet name',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
            }),
            'photo': forms.URLInput(attrs={
                'placeholder': 'Link to image',
            }),
        }

        labels = {
            'name': 'Pet name',
            'date_of_birth': 'Date of Birth',
            'photo': 'Link to Image',
        }


class PetEditForm(PetForm):

    readonly_fields = ('date_of_birth',)

    def clean_date_of_birth(self):
        # date_of_birth = self.cleaned_data["date_of_birth"]
        # if date_of_birth != self.instance.date_of_birth:
        #     raise ValidationError("Date of birth is readonly")

        return self.instance.date_of_birth


class PetDeleteForm(PetForm):

    readonly_fields = ('date_of_birth', 'name', 'photo', )

    def save(self, commit=False):
        if commit:
            # If no cascade
            # self.instance.comment.delete()
            # self.instance.likes.delete()
            self.instance.delete()
        return self.instance

