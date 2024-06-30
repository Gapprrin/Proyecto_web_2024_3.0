from datetime import datetime
from django.db import models
from django.contrib.auth.forms import User


# Create your models here.
class Producto(models.Model):
    id = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    oferta = models.BooleanField()
    imagen = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

# class User(models.Model):
#     id = models.AutoField(primary_key = True)
#     user_name = models.CharField(max_length = 30)
#     user_mail = models.CharField(max_length = 60)
#     user_pass = models.CharField(max_length = 10)
#     user_commune = models.CharField(max_length = 25)
    
#     def __str__(self):
#         return self.user_name
#     #abstract user
#     # AUTH_USER_MODEL= "user.CustomUser"



class NuevaColeccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_auto = models.CharField(max_length=40)
    descripcion_auto = models.CharField(max_length=200)
    stock_auto = models.IntegerField()
    imagen_auto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_auto

    class Meta:
        db_table = 'nueva_coleccion'  # Especifica el nombre de la tabla


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCategoria
    
class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_vehiculo = models.CharField(max_length=50)
    descripcion_vehiculo = models.CharField(max_length=200)
    stock_vehiculo = models.IntegerField()
    imagen_vehiculo = models.CharField(max_length=255)
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_vehiculo


class Accesorios_desc(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_accesorio = models.CharField(max_length=50)
    descripcion_accesorio = models.CharField(max_length=200)
    precio_accesorio = models.IntegerField()
    stock_accesorio = models.IntegerField()
    imagen_accesorio= models.CharField(max_length=255)
  

    def __str__(self):
        return self.nombre_accesorio
    

class CategoriaAccesorios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria_acc = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria_acc
    
class Accesorios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_acc = models.CharField(max_length=50)
    precio_acc= models.IntegerField()
    descripcion_acc = models.CharField(max_length=200)
    stock_acc = models.IntegerField()
    imagen_acc = models.CharField(max_length=255)
    categoria = models.ForeignKey(to=CategoriaAccesorios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_acc
    
    
class Boleta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_compra = models.DateTimeField(default= datetime.now, blank=True)
    usuario = models.ForeignKey(to= User, on_delete=models.CASCADE)
    monto_total = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.usuario.username}'

class DetalleBoleta(models.Model):
    producto = models.ForeignKey(to=Accesorios, on_delete=models.CASCADE)
    boleta = models.ForeignKey(to= Boleta, on_delete=models.CASCADE)
    precio_prod = models.IntegerField()
    cantidad_prod = models.IntegerField()

    def __str__(self):
        return f'{self.producto.nombre_acc} {self.boleta.id}'