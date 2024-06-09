from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Feedback', 'rows': 3, 'required': True}),
        }
        labels = {
            'name': '',
            'email': '',
            'feedback': '',
        }