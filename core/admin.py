from django.contrib import admin

from .models import *



# Register your models here.
admin.site.register(Producto)


admin.site.register(Categoria) 

admin.site.register(Vehiculo) 

admin.site.register(NuevaColeccion) 

admin.site.register(Accesorios_desc) 

admin.site.register(CategoriaAccesorios) 

admin.site.register(Accesorios) 
