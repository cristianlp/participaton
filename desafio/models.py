from django.db import models
from taggit.managers import TaggableManager


from usuario.models import Usuario
from convocatoria.models import Convocatoria

def desafio_directory_path(instance, filename):
    # archivo cargado en MEDIA_ROOT/desafio_<id>/<filename>
    return 'desafio_{0}/{1}'.format(instance.desafio.id, filename)


class Documento(models.Model):
    descripcion = models.CharField(max_length=255, blank=True)
    documento = models.FileField(upload_to=desafio_directory_path)
    subido_el = models.DateTimeField(auto_now_add=True)
    subido_por = models.ForeignKey(Usuario)
    desafio = models.ForeignKey("Desafio")


class Desafio(models.Model):

    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    objetivos = models.TextField(blank=True, null=True)

    #votos
    votable = models.BooleanField(default=False)
    
    #modo borrador (false)/publicado (true)
    publicado = models.BooleanField(default=False)

    tematicas = TaggableManager()

    convocatoria = models.ForeignKey(Convocatoria)


    creado_el = models.DateTimeField(auto_now_add=True)
    actualizado_el = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "desafio"
        verbose_name_plural = "desafios"