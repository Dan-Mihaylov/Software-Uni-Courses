from django import forms

from ..photos.models import Comment


class CommentAddForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
            }),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...'
            },
        ),
        required=False,
    )

