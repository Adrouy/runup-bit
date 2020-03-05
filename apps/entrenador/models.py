from django.db import models

# Create your models here.

# Create your models here.
# No coloco id ya que djnago automaticamente coloca un campo id autoincrementable en la base de datos. 
# En caso de que queramos tener una primary_key debería ser por ejemplo: ci = models.IntegerField(primary_key=True)


class Plan_entrenamiento(models.Model):
    nombre_entrenamiento = models.CharField(max_length=50)
    ejercicio1 = models.CharField (max_length=50)
    ejercicio2 = models.CharField (max_length=50)
    ejercicio3 = models.CharField (max_length=50)
    ejercicio4 = models.CharField (max_length=50)
    ejercicio5 = models.CharField (max_length=50)
    ejercicio6 = models.CharField (max_length=50)
    ejercicio7 = models.CharField (max_length=50)



class Entrenador(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre_entrenador = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    domicilio: models.TextField()
    description = models.TextField()
    plan = models.ManyToManyField(Plan_entrenamiento)