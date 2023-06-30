from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tipo, Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Tipo)