from django.forms import ModelForm, Textarea

from convocatoria.models import Convocatoria


class ConvocatoriaNuevoForm(ModelForm):
	class Meta:
		model = Convocatoria
		fields = ['titulo', 'descripcion', 'lugar', 'fecha_desde', 'fecha_hasta']


class ConvocatoriaNuevoP1Form(ModelForm):
	class Meta:
		model = Convocatoria
		fields = ['titulo', 'descripcion', 'lugar', 'fecha_desde', 'fecha_hasta']


class ConvocatoriaNuevoP2Form(ModelForm):
	class Meta:
		model = Convocatoria
		fields = ['imagen', 'publicada']
