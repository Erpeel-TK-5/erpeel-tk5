from django import forms

class EditForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.CharField(label='Age', max_length=100)
    description = forms.CharField(label='Description', max_length=100)