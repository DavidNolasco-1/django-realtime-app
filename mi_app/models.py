from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    cantidad = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nombre
