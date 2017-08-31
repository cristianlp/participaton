from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required

from convocatoria.models import Convocatoria
from .forms import ConvocatoriaNuevoP1Form, ConvocatoriaNuevoP2Form

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