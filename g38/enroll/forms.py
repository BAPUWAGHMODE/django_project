from django import forms
from enroll.models import employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class employeeregistarion(forms.ModelForm):
    class Meta:
        model=employee
        fields=['em_name','em_email','img','pdf']

class employeeregistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
