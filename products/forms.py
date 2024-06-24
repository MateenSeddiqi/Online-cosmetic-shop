from django import forms
from .models import Feedback, Product

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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','company', 'cost', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company', 'required': True}),
            'cost': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cost', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }
        labels = {
            'name': '',
            'company': '',
            'cost': '',
            'image': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
