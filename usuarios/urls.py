from django.urls import path
from . import views



urlpatterns=[
    path('', views.index, name="index"),
    path('catalInal', views.catalInal, name="catalInal"),
    path('catalElec', views.catalElec, name="catalElec"),
    path('catalAcce', views.catalAcce, name="catalAcce"),
    path('carrito', views.carrito, name="carrito"),
    path('quienSomos', views.quienSomos, name="quienSomos"),
    path('registro', views.registro, name="registro"),
]