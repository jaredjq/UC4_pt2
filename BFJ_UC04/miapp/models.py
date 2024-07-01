from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    codigo = models.CharField(max_length=100)
    dni = models.TextField()
    nombre = models.TextField()
    apepat = models.TextField()
    apemat = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    estado = models.TextField()
    # auto_now_add me permitirá registrar 
    # la fecha cuando cree el registro
    creado = models.DateTimeField(auto_now_add=True)
    # auto_now me permitirá registrar 
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

