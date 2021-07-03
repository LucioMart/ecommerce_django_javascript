from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "ecommerceApp/home.html")#HttpResponse("Home")

def servicios(request):
    return render(request, "ecommerceApp/servicios.html") #HttpResponse("Servicios")

def tienda(request):
    return render(request, "ecommerceApp/tienda.html") #HttpResponse("Tienda")

def blog(request):
    return render(request, "ecommerceApp/blog.html") #HttpResponse("Blog")

def contacto(request):
    return render(request, "ecommerceApp/contacto.html") #HttpResponse("Contacto")