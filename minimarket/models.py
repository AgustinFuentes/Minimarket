from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    def disminuir_cantidad(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            self.save()
