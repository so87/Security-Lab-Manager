from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from slmApp.models import Exercises,Classes,CustomUser,Submissions
from django import forms
from django.forms import ModelForm
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {'username': ('Your username'), 'password': ('Your Password')}
        help_texts = {'username': ('Your username...'), 'password': ('Your password...')}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username...'}),
            'password': forms.TextInput(attrs={'placeholder': 'Enter your password...'})
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SubmitAnswer(forms.Form):
    submitted = forms.CharField(max_length=50)