from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


class Ciudad(models.Model):
	ciudad = models.CharField(max_length=250)


def convocatoria_directory_path(instance, filename):
    # archivo cargado en MEDIA_ROOT/convocatoria_<id>/<filename>
    return 'convocatoria_{0}/{1}'.format(instance.convocatoria.id, filename)


class Convocatoria(models.Model):
	titulo = models.CharField(max_length=250)
	descripcion = models.TextField()
	lugar = models.CharField(max_length=250)
	ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
	fecha_desde = models.DateField()
	fecha_hasta = models.DateField()
	publicada = models.BooleanField(default=False)

	tematicas = TaggableManager()

	#En caso que las convocatorias tengan un premio
	premio = models.BooleanField(default=False)
	premio_descripcion = models.TextField(blank=True, null=True)

	imagen = models.ImageField(upload_to = 'images/', default = 'images/no-img.png')

	creada_el = models.DateTimeField(auto_now_add=True)
	actualizada_el = models.DateTimeField(blank=True, null=True)


	def get_absolute_url(self):
		return reverse('padmin:convocatoria_desafios', args=[str(self.id)])


	def tematicas(self, obj):
		return u", ".join(o.name for o in obj.tematicas.all())
	
	class Meta:
		ordering = ['fecha_hasta']        