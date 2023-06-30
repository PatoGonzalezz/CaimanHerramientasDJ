from .models import Producto
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["producto",]
        labels = {"producto":"Producto",}