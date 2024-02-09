from django import forms

from .models import Photo
from ..mixins.form_mixins import ReadOnlyFieldFormMixin


class BasePhotoForm(forms.ModelForm, ReadOnlyFieldFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    class Meta:
        model = Photo
        exclude = ['created_on', 'modified_on']


class CreatePhotoForm(BasePhotoForm):
    pass


class EditPhotoForm(BasePhotoForm):
    pass


class DeletePhotoForm(BasePhotoForm):

    class Meta(BasePhotoForm.Meta):
        fields = ['id', 'description', 'location', 'tagged_pets']

    readonly_fields = ('description', 'location', 'tagged_pets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=False):
        if commit:
            self.instance.delete()
        return self.instance
