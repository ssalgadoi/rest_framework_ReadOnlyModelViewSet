from django.db import models

# Create your models here.

#API CLIMA

CLIMA = [
    [0,"Soleado"],
    [1,"Luvia"],
    [2,"Nublado"],
    [3,"Nieve"],
]


class Descripcion(models.Model):

    descripcion_clima = models.IntegerField(choices=CLIMA, default=0)
    temperatura = models.FloatField()
    crear_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-crear_en']

