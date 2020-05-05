from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('username', 'email', 'text')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'feedback_form', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'feedback_form', 'placeholder': 'Email'}),
            'text': forms.TextInput(attrs={'class': 'feedback_form', 'placeholder': 'Text'})
        }
