from django import forms
from django.contrib.auth.models import User
import re

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username_value = self.cleaned_data['username']
        if len(username_value) < 3:
            raise forms.ValidationError('username must be at least 3 characters long.')
        return username_value

    def clean_password(self):
        password_value = self.cleaned_data['password']
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:,<.>]).{8,}$')
        if not password_pattern.match(password_value):
            raise forms.ValidationError('Please set a Strong Password')
        return password_value
    
class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    
