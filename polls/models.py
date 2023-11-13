import datetime

from django.db import models
from django.utils import timezone

class Pregunta (models.Model):
    texto_pregunta = models.CharField(max_length = 200)  # una columna en BD
    fecha_publicacion = models.DateTimeField("fecha publicada")  # otra columna en BD
    
    def __str__(self):
        return self.texto_pregunta
    
    def publicado_reciente(self):
        return self.fecha_publicacion >= (timezone.now() - datetime.timedelta(days = 1))


class Opcion (models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
    texto_opcion = models.CharField(max_length = 200)
    votos = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.texto_opcion