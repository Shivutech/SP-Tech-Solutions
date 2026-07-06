from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'email',
            'phone',
            'service',
            'budget',
            'message',
            'project_file',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),

            'service': forms.Select(attrs={
                'class': 'form-select'
            }),

            'budget': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Budget'
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Project Details'
            }),
            
            'project_file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        } 
        