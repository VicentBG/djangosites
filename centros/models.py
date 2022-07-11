from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Bono(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    centro = models.CharField(max_length=5)
    nombre_centro = models.CharField(max_length=60)
    agente = models.CharField(max_length=3)
    nombre_agente = models.CharField(max_length=60)
    codpost = models.CharField(max_length=5)
    poblacion = models.CharField(max_length=60)
    created_at = models.DateTimeField(default=now())

    def __str__(self) -> str:
        return 'Bono nº: ' + self.codigo + ' del centro GdC: ' + str(self.centro) + '-' + self.nombre_centro

