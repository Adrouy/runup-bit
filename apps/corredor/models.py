from django.db import models

# Create your models here.
from apps.entrenador.models import Entrenador

class Corredor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre_corredor = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    peso_kg = models.IntegerField()
    altura_mts = models.IntegerField()
    fecha_nacimiento = models.DateField()
    celular = models.CharField(max_length=13)
    email = models.EmailField()
    domicilio = models.TextField()
    description = models.TextField()
    nombre_entrenador = models.ForeignKey(Entrenador, null=True, blank=True, on_delete=models.CASCADE)