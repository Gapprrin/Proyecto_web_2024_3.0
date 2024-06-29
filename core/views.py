
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.

from .models import NuevaColeccion

def home(request):
    nueva_coleccion = NuevaColeccion.objects.all()
    accesorios_desc = Accesorios_desc.objects.all()
    
    contexto1 = {
       'nueva_coleccion': nueva_coleccion,
       'accesorios_desc': accesorios_desc
        
    }
    
    
    return render(request, 'index.html', contexto1)

def modelos(request):
    nueva_coleccion = NuevaColeccion.objects.all()
    vehiculos_deportivos = Vehiculo.objects.filter(categoria__nombreCategoria='Deportivo')
    vehiculos_familiares = Vehiculo.objects.filter(categoria__nombreCategoria='Familiar') 
    vehiculos_electricos = Vehiculo.objects.filter(categoria__nombreCategoria='Electrico')
   
    
    contexto = {
        'nueva_coleccion': nueva_coleccion,
        'vehiculos_deportivos': vehiculos_deportivos,
        'vehiculos_familiares': vehiculos_familiares,
        'vehiculos_electricos': vehiculos_electricos,
     
     
    }
    return render(request, 'Pages/modelos.html', contexto)

# Iniciar sesión

def login(request):
    user = User.objects.all()
    return render(request, 'Pages/login.html', {'user':user})

# Cerrar sesión

def logout(request):
    return logout_then_login(request, 'login')


# Crear cuenta

def createAccount(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'Pages/Create_account.html', {'form' : registro})

# carrito

def shopKart(request):
    return render(request, 'Pages/Carrito.html')

# Agregar al carrito

def addToShopKart(request, id):
    accesorio = Accesorios.objects.get(id = id)
    carrito = request.session.get("carrito", [])
    monto = request.session.get("monto", [{"subtotal" : 0, "total" : 0}])
    for item in carrito:
        if item["id"] == id:
            monto[0]["subtotal"] -= item["subtotal"]
            monto[0]["total"] -= item["subtotal"]
            item["cantidad"] += 1
            item["subtotal"] = item["precio"] * item["cantidad"]
            monto[0]["subtotal"] += item["subtotal"]
            monto[0]["total"] += item["subtotal"]
            break
    else:
        carrito.append({"id" : id, "nombre" : accesorio.nombre_acc, "imagen" : accesorio.imagen_acc,
                        "cantidad" : 1, "precio" : accesorio.precio_acc, "subtotal" : accesorio.precio_acc})
        monto[0]["subtotal"] += accesorio.precio_acc
        monto[0]["total"] += accesorio.precio_acc
    request.session["carrito"] = carrito
    request.session["monto"] = monto
    return redirect(to='accesorios')

# Eliminar del carrito

def removeFromShopKart(request, id):
    carrito = request.session.get("carrito", [])
    monto = request.session.get("monto", [{"subtotal" : 0, "total" : 0}])
    for item in carrito:
        if item["id"] == id:
            if item["cantidad"] > 1:
                monto[0]["subtotal"] -= item["subtotal"]
                monto[0]["total"] -= item["subtotal"]
                item["cantidad"] -= 1
                item["subtotal"] = item["precio"] * item["cantidad"]
                monto[0]["subtotal"] += item["subtotal"]
                monto[0]["total"] += item["subtotal"]
                break
            else:
                carrito.remove(item)
                monto[0]["subtotal"] -= item["precio"]
                monto[0]["total"] -= item["precio"]
    request.session["carrito"] = carrito
    request.session["monto"] = monto
    return redirect(to="Carrito")


def accesorios(request):
    accesorios = Accesorios.objects.all()
    interior = Accesorios.objects.filter(categoria__nombre_categoria_acc='Interior')
    exterior = Accesorios.objects.filter(categoria__nombre_categoria_acc='Exterior')
    ruedas_neumaticos = Accesorios.objects.filter(categoria__nombre_categoria_acc='Ruedas y neumáticos')
   
    contexto = {
        'accesorios': accesorios,
        'interior': interior,
        'exterior': exterior,
        'ruedas_neumaticos': ruedas_neumaticos,
    }
    return render(request, 'Pages/accesorios.html', contexto)


def acerca_de(request):
    return render(request, 'Pages/acerca_de.html') 

