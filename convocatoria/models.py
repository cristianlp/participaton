from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


class Ciudad(models.Model):
	ciudad = models.CharField(max_length=250)


class Convocatoria(models.Model):
	titulo = models.CharField(max_length=250)
	descripcion = models.TextField()
	lugar = models.CharField(max_length=250)
	ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
	fecha_desde = models.DateField()
	fecha_hasta = models.DateField()
	publicada = models.BooleanField(default=False)

	tematicas = TaggableManager()

	imagen = models.ImageField(upload_to = 'images/', default = 'images/no-img.png')

	creada_el = models.DateTimeField(auto_now_add=True)
	actualizada_el = models.DateTimeField(blank=True, null=True)


	def get_absolute_url(self):
		return reverse('convocatoria_detail', args=[str(self.id)])


	def tematicas(self, obj):
		return u", ".join(o.name for o in obj.tematicas.all())
	
	class Meta:
		ordering = ['fecha_hasta']        