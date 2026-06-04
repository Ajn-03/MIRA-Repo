from django import forms
from .models import User_Info
from django.core.exceptions import ValidationError
from django.utils import timezone

        
class Blood_Sample(forms.ModelForm):
    class Meta:
        model=User_Info
        fields=('user_name','email_add','dob','glucose','haemoglobin','cholesterol')
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }       

