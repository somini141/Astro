from django import forms
from .models import SiteUser


class SiteUserForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ['full_name', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ваше полное имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваш email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш телефон'}),
        }
