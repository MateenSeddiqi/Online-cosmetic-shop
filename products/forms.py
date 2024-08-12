from django import forms
from .models import Feedback, Product, contactUs

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
            'name': 'Name',
            'email': 'Email Address',
            'feedback': 'Your feedback',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','company', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }
        labels = {
            'name': 'Product Name',
            'company': 'Company Name',
            'price': 'Price',
            'image': 'Image',
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)
        if instance and instance.image:
            self.fields['image'].required = False
        else:
            self.fields['image'].required = True

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'required': True}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'message': 'Your Message',
        }