from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


from django.contrib.auth.decorators import login_required

from .models import Convocatoria


class HomeView(TemplateView):

	template_name = "convocatoria/index.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		convocatorias = Convocatoria.objects.all()
		context['convocatorias'] = convocatorias

		return context
		
		

