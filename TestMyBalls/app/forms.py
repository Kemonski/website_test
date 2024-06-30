from django import forms
from .models import UsagiInfo

class UsagiInfoForm(forms.ModelForm):
    class Meta:
        model = UsagiInfo
        fields = ['user', 'firstname', 'lastname', 'contact_number', 'email', 'gender', 'country', 'language']
