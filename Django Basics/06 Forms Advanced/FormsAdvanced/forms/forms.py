from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.forms import formset_factory, modelform_factory
from django.urls import reverse

from .models import Person



'''
In order to add more args or kwargs to the ModelForm you have to do the __init__ method first, and then add the Meta
class.
'''
class PersonForm(forms.ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = Person
        exclude = ('created_by', )

        labels = {
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
        }

        '''
        The most common methods to be overriden, and filled with custom logic are the save() method
        and the clean() method. In the save() method, we mostly use it to attach instances to the FK, fields
        or to the m2m fields and so on.
        
        The clean method, we use it to do stuff with the cleaned data, or attach and customize the validators,
        create new validation logic and so on.
        '''

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
            instance.save()
        return instance



class ReadonlyFieldsMixin:
    readonly_fields = ()    # <-- Create an attribute, where you will specify which fields will be read only

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'


class BootstrapFormMixin:

    def _add_bootstrap_to_fields(self):
        for field_name, field in self.fields:
            field.widget.attrs['class'] = 'form-control'


class UpdatePersonForm(ReadonlyFieldsMixin, PersonForm):

    readonly_fields = ('age', 'last_name',)

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        self._mark_readonly_fields()


