from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.shortcuts import get_object_or_404

from django.core import serializers

from convocatoria.models import Convocatoria
from desafio.models import Desafio
from .forms import ConvocatoriaNuevoForm, ConvocatoriaNuevoP1Form, ConvocatoriaNuevoP2Form

class HomeView(ListView):

	model = Convocatoria
	template_name = "padmin/index.html"


class ConvocatoriaDetailView(DetailView):
	model = Convocatoria
	template_name = 'padmin/convocatoria_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ConvocatoriaDetailView, self).get_context_data(**kwargs)
		#context['now'] = timezone.now()
		return context

class ConvocatoriaEditView(UpdateView):
	model = Convocatoria
	template_name = 'padmin/convocatoria_edit.html'
	fields = ['titulo', 'descripcion', 'lugar', 'ciudad', 'fecha_desde', 'fecha_hasta']
	#actualizar campo actualizado_el


class ConvocatoriaNuevoView(CreateView):
	model = Convocatoria
	template_name = 'padmin/convocatoria_new.html'  
	form_class = ConvocatoriaNuevoForm
	#success_url = '/padmin/convocatoria/view/'


	def get_success_url(self):
		print(dir(self))
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.save()
		return super(ConvocatoriaNuevoView, self).form_valid(form)


class ConvocatoriaNuevoP1View(FormView):
	template_name = 'padmin/convocatoria_new_p1.html'  #paso 1
	form_class = ConvocatoriaNuevoP1Form
	success_url = '/padmin/convocatoria/new/2/'

	def form_valid(self, form):
		form.save()

		return super(ConvocatoriaNuevoP1View, self).form_valid(form)

class ConvocatoriaNuevoP2View(FormView):
	template_name = 'padmin/convocatoria_new_p2.html'  #paso 1
	form_class = ConvocatoriaNuevoP2Form
	success_url = '/'

	def form_valid(self, form):
		form.save()

		return super(ConvocatoriaNuevoP2View, self).form_valid(form)		


#Vistas basadas en funciones *************************************************
def convocatoria_desafios(request, convocatoria_id):
	convocatoria = Convocatoria.objects.get(id=convocatoria_id)
	desafios = Desafio.objects.filter(convocatoria=convocatoria_id)
	data = {
		'convocatoria': convocatoria,
		'desafios': desafios
	}

	return render(request, 'padmin/convocatoria_desafios.html', data)



def convocatoria_publicar(request, convocatoria_id):
	convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)
	convocatoria.publicada=True
	convocatoria.save()

	data = {
			'publicada': True
	}

	return JsonResponse(data)



