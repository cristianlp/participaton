from django.forms import ModelForm

from desafio.models import Desafio



class DesafioNuevoForm(ModelForm):
	class Meta:
		model = Desafio
		fields = ['titulo', 'descripcion', 'objetivos']
