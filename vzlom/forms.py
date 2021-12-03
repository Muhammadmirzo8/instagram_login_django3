from django import forms
from django.forms import fields 
from .models import Userbek
class Userform(forms.ModelForm): 
    class Meta: 
        model = Userbek
        fields = '__all__'