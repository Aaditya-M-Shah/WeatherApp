from .models import *
from django.forms import ModelForm, TextInput

class Cityform(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        widgets = {"name":TextInput(attrs={"class":"input","placeholder":"Add city"})}