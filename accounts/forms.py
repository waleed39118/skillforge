# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            self.add_error('confirm_password', 'Passwords do not match.')
        return cleaned
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Email is already in use.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')