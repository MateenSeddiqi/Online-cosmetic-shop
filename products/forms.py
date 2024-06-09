from django import forms
from .models import Feedback

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'feedback']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
#             'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': True}),
#         }
#         labels = {
#             'name': 'Name',
#             'email': 'Email address',
#             'feedback': 'Feedback',
#         }
#         help_texts = {
#             'email': 'We\'ll never share your email with anyone else.',
#         }
