from .models import Producto
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["producto",]
        labels = {"producto":"Producto",}

class CustomUserCreationForm(UserCreationForm):
    pass