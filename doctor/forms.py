from django import forms
from .models import Doctor, Patient
from django.forms import ModelForm


class LoginForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput
        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  # or __all__
        labels = {
            'salutation': 'Salutation',
            'firstname': 'Firstname',
            'lastname': 'Lastname',
            'gender': 'Gender',
            'age': 'Age',
            'identitynum': 'NRIC/FIN',
            'email': 'Email',
            'contactnum': 'Contact Number',
            'allergies': 'Allergies',
            'medhistory': 'Medical History',
        }
        widgets = {
            'salutation': forms.Select(choices=[('Mr', 'Mr'), ('Ms', 'Ms'), ('Mdm', 'Mdm'), ('Mrs', 'Mrs'), ('Others', 'Others')]),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]),
            'allergies': forms.Textarea(attrs={
                'rows': '6',
                'cols': '80',
            }),
            'medhistory': forms.Textarea(attrs={
                'rows': '6',
                'cols': '80',
            })
        }
