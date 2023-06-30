from django.urls import path
from . import views

urlpatterns=[
    path('listaProds', views.lista_productos, name='lista_productos'),
    path('addProd', views.agregar_productos, name='addProd'),
    path('deletProd/<str:pk>', views.eliminar_productos, name='delete_producto'),
    path('findProd/<str:pk>', views.buscar_productos, name='editar_ProductFind'),
    path('editProd', views.actualizar_productos, name="actualizar_productos"),
    path('', views.menu, name='menu'),
]