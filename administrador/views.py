from django.shortcuts import render
from .models import Tipo, Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.
@login_required
def menu (request):
    request.session["usuario"]="caiman"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, "indexCRUD.html",context)

@login_required
def inicio (request):
    lista_productos = Producto.objects.all()
    context={"productos":lista_productos}
    return  render(request,'inicioadmin.html', context)

def lista_productos(request):
    lista_productos = Producto.objects.raw("SELECT * FROM administrador_Producto")
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator (lista_productos, 5)
        lista_productos = paginator.page(page)
    except:
        raise Http404
    context = {"productos":lista_productos}
    return render(request,'inicioadmin.html',context)


def agregar_productos(request):
    if request.method != "POST":
        lista_tipo =  Tipo.objects.all()
        context =  {"tipos":lista_tipo}
        return render(request, 'productos_add.html', context)
    else:
        id_prod         = request.POST["id"]
        nombre_prod     = request.POST["nombre"]
        marca_prod      = request.POST["marca"]
        tipo            = request.POST["tipo"]
        precio_prod     = request.POST["precio"]
        stock_prod      = request.POST["stock"]

        objTipoProducto =  Tipo.objects.get(id_tipo = tipo)
        objProducto     = Producto.objects.create(
            id_producto     = id_prod,
            nombre          = nombre_prod,
            marca           = marca_prod,
            id_tipo         = objTipoProducto,
            precio          = precio_prod,
            stock           = stock_prod)

        objProducto.save()
        messages.success(request, "Producto Agregado")
        lista_tipo = Tipo.objects.all()
        context = {"tipos":lista_tipo}
        return render(request, 'inicioadmin.html',context)

def eliminar_productos(request,pk):
    
    try:
        producto = Producto.objects.get(id_producto=pk)
        producto.delete() #delete en la BD
        messages.success(request,"Producto Eliminado")
        lista_producto = Producto.objects.all()
        context={"Producto":lista_producto}
        return render(request,'inicioadmin.html',context)
    except:
        lista_producto = Producto.objects.all()
        context={"producto":lista_producto}
        return render(request,'inicioadmin.html',context)

def buscar_productos(request,pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        tipos = Tipo.objects.all()
        context={"producto":producto, "tipos":tipos}
        if producto:
            return render(request,'productos_edit.html', context)
        else:
            context = {"mensaje":"El producto no existe"}
            return render(request,'inicioadmin.html',context)    

def actualizar_productos(request):
    
    if request.method == "POST":
        #rescatamos en variables los valores del formulario (name)
        id_prod         = request.POST["id"]
        nombre_prod     = request.POST["nombre"]
        marca_prod      = request.POST["marca"]
        tipo            = request.POST["tipo"]
        precio_prod     = request.POST["precio"]
        stock_prod      = request.POST["stock"]

        objTipo = Tipo.objects.get(id_tipo = tipo)
        #crea Producto (izd: nombre del campo de la BD, derecho: variable local)
        objProducto = Producto()
        objProducto.id_producto   = id_prod
        objProducto.nombre        = nombre_prod
        objProducto.marca         = marca_prod
        objProducto.id_tipo       = objTipo
        objProducto.precio        = precio_prod
        objProducto.stock         = stock_prod
        
        objProducto.save() #update en la base de datos
        messages.success(request, "Producto Actualizado")
        lista_tipo = Tipo.objects.all()
        context = {"tipos":lista_tipo}
        return render(request,'inicioadmin.html',context)
    else:
        lista_Producto = Producto.objects.all()
        context = {"Productos":lista_Producto}
        return render(request,'productos_edit.html',context)        

