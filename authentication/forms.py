from django import forms
from django.utils.translation import get_language

class LoginForm(forms.Form):
    username=forms.CharField(label='Username/Email',max_length=50)
    password=forms.CharField(label='Password',widget=forms.PasswordInput, max_length = 50)

class RegisterForm(forms.Form):
    name_label = ""
    if get_language == "id":
        name_label = "Nama"
    else:
        name_label = "Name"
    username = forms.CharField(label='Username', max_length=50)
    name = forms.CharField(label=name_label, max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=20)