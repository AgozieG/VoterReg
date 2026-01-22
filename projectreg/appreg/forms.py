# app/forms.py
from django import forms
from .models import Voter


class VoterForm(forms.ModelForm):
    


    class Meta:
        model = Voter
        fields = ['surname','firstname','dob','email','gender','phone','marital_status','rc_number','mine_name']
        widgets = {
        'surname': forms.TextInput(attrs={'placeholder':'Surname','required':True}),
        'firstname': forms.TextInput(attrs={'placeholder':'First name','required':True}),
        'dob': forms.DateInput(attrs={'type':'date'}),
        'email': forms.EmailInput(attrs={'placeholder':'email@example.com'}),
        'phone': forms.TextInput(attrs={'placeholder':'+234...'}),
        'rc_number': forms.TextInput(attrs={'placeholder':'Enter your RC Number','required':True}),
        'mine_name': forms.TextInput(attrs={'placeholder':'Name of farm'}),
        }