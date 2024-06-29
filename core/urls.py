
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name= "home"),
    path('modelos/', modelos, name= "modelos"),
    path('login/', LoginView.as_view(template_name="pages/login.html"), name= "login"),
    path('logon/', createAccount, name= "create_account"),
    path('logout', logout, name="logout"),
    path('shopKart/', shopKart, name= 'Carrito'),
    path('addToShopKart/<id>', addToShopKart, name= 'addToShopKart'),
    path('removeFromShopKart/<id>', removeFromShopKart, name= 'removeFromShopKart'),
   path('accesorios/', accesorios, name='accesorios'),
    path('acerca_de/', acerca_de, name="acerca_de"),

]  