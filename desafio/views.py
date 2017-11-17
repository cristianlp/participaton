from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.core import serializers

from convocatoria.models import Convocatoria
from .models import Desafio
from .forms import DesafioNuevoForm

def get_desafios(request, convocatoria_id):
	if request.method == "GET":
		if request.is_ajax():
			desafios = Desafio.objects.all().values('id', 'titulo', 'descripcion')
			
			return JsonResponse({'results': list(desafios)})			


def desafio_new(request):

	if request.method == "POST":

		if request.is_ajax():
			convocatoria_id= request.POST.get('convocatoria_id')
			titulo = request.POST.get('titulo')
			descripcion = request.POST.get('descripcion')

			convocatoria = Convocatoria.objects.get(id=convocatoria_id)

			desafio = Desafio(titulo=titulo, descripcion=descripcion, convocatoria=convocatoria)
			desafio.convocatoria = convocatoria
			desafio.save()

			#desafios = Desafio.objects.all().values('id', 'titulo','descripcion')

			#response=serializers.serialize('json', desafios, fields=('titulo'))

			return JsonResponse({'results': list(Desafio.objects.filter(id=desafio.id).values('id', 'titulo', 'descripcion'))})

	else:

		return render(request, 'desafio/desafio_new.html', {})