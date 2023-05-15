from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_lenght=100)
    apellido = models.CharField(max_lenght=50)
    nroDNI = models.PositiveBigIntegerField()
    telefono = models.PositiveBigIntegerField()
    email = models.CharField(max_lenght=100)
    is_active = models.BooleanField(default=True)