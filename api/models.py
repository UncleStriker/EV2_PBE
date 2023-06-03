from django.db import models

# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipoAnimal = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
