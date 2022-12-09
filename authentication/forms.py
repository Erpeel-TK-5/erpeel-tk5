from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label='Username/Email',max_length=50)
    password=forms.CharField(label='Password',widget=forms.PasswordInput, max_length = 50)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    name = forms.CharField(label='Nama', max_length=50)
    email = forms.CharField(label='Email', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=20)