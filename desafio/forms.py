from django import forms
from django.forms import ModelForm

from desafio.models import Desafio



class UploadDocumentoForm(forms.Form):
	descripcion = forms.TextField()
	documento = forms.FileField()


class DesafioNuevoForm(ModelForm):
	class Meta:
		model = Desafio
		fields = ['titulo', 'descripcion', 'objetivos']
