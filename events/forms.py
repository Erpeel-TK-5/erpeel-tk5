from django import forms

class EventForm(forms.Form):
    name=forms.CharField(label='Nama-Event',max_length=50)
    start_date=forms.DateField(label='Start-Date',widget=forms.DateInput(attrs={'type': 'date'}))
    end_date=forms.DateField(label='End-Date',widget=forms.DateInput(attrs={'type': 'date'}))
    is_public=forms.BooleanField(label='Is-Public',widget=forms.CheckboxInput, required=False)
    is_recurring=forms.BooleanField(label='Is-Recurring',widget=forms.CheckboxInput, required=False)
    notes=forms.CharField(label='Notes',max_length=1000)