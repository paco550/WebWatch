from django.db import models

# Create your models here.
class SitioWeb(models.Model):
    url = models.URLField(unique=True)
    estado = models.CharField(max_length=20, default="Desconocido")
    tiempo_respuesta = models.FloatField(null=True, blank=True)
    ultimo_chequeo = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url