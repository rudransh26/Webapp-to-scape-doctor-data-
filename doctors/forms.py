from django import forms

class inpform(forms.Form):
    city = forms.CharField(max_length=50)
    specialization = forms.CharField(max_length=50)
