from slmApp.models import Users,Exercises,Classes
from django import forms
from django.forms import ModelForm
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']
        labels = {'email': ('Your Email Address'), 'password': ('Your Password')}
        help_texts = {'email': ('Your email...'), 'password': ('Your password...')}
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email...'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter your password...'})
        }