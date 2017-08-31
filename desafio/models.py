from django.db import models
from taggit.managers import TaggableManager


from usuario.models import Usuario
from convocatoria.models import Convocatoria


class Desafio(models.Model):

    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    contexto = models.TextField(blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)

    #votos
    votable = models.BooleanField(default=False)
    
    #modo borrador (false)/publicado (true)
    publicado = models.BooleanField(default=False)

    tematicas = TaggableManager()

    convocatoria = models.ForeignKey(Convocatoria)


    creado_el = models.DateTimeField()
    actualizado_el = models.DateTimeField()


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "desafio"
        verbose_name_plural = "desafios"