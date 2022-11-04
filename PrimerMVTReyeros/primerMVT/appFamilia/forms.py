from django import forms

class FamiliaForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    fNacimiento=forms.CharField(max_length=7)
    edad=forms.IntegerField()