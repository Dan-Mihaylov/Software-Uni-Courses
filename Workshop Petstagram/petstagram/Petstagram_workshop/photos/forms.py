from django import forms

from .models import Photo
from ..mixins.form_mixins import ReadOnlyFieldFormMixin, DisabledFieldFormMixin


class BasePhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['created_on', 'modified_on']


class CreatePhotoForm(BasePhotoForm):
    pass


class EditPhotoForm(ReadOnlyFieldFormMixin, DisabledFieldFormMixin, BasePhotoForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
        self._apply_disabled_on_fields()

    pass


class DeletePhotoForm(ReadOnlyFieldFormMixin, DisabledFieldFormMixin, BasePhotoForm):

    readonly_fields = ('description', 'location',)
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
        self._apply_disabled_on_fields()

    class Meta(BasePhotoForm.Meta):
        fields = ['id', 'description', 'location', 'tagged_pets']

    def save(self, commit=False):
        if commit:
            self.instance.delete()
        return self.instance
