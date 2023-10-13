from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):
    return render(request, "foodShop/home.html")


def Servicios(request):
    return render(request, "foodShop/servicios.html")

def Tienda(request):
    return render(request, "foodShop/tienda.html")

def Blog(request):
    return render(request, "foodShop/blog.html")

def Contacto(request):
    return render(request, "foodShop/contacto.html")

