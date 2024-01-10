from django import forms


class RecommendationForm(forms.Form):
    name = forms.CharField(max_length=20)
    recommendation = forms.CharField(widget=forms.Textarea, label='Recommendation')

    class Meta:
        widgets = {
            # 'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'recommendation': forms.Textarea(attrs={'placeholder': 'Recommendations'}),
        }
