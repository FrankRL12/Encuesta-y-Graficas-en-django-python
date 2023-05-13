from django.db import models

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    mayor_de_edad = models.CharField(max_length=2)
    sabor_p = models.CharField(max_length=10)
    calidad_p = models.CharField(max_length=10)
    formato_p = models.CharField(max_length=10)
    recomendar_p = models.CharField(max_length=2)

 