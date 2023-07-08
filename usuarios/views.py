from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def quienSomos(request):
    return render(request, "about.html")

def registro(request):
    return render(request, "register.html")

def catalInal (request):
    return render(request, "main-inal.html")

def catalElec (request):
    return render(request, "main-elec.html")

def catalAcce (request):
    return render(request, "main-acceso.html")

def carrito(request):
    return render(request, "shop.html")

