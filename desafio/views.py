from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST

from django.core.urlresolvers import reverse

from django.core import serializers

from convocatoria.models import Convocatoria
from .models import Desafio, Documento
from .forms import DesafioNuevoForm, UploadDocumentoForm



def get_desafios(request, convocatoria_id):
	if request.method == "GET":
		if request.is_ajax():
			desafios = Desafio.objects.filter(convocatoria=convocatoria_id).values('id', 'titulo', 'descripcion')
			
			return JsonResponse({'results': list(desafios)})			


def desafio_new(request):

	if request.method == "POST":

		convocatoria_id= request.POST.get('convocatoria_id')
		titulo = request.POST.get('titulo')
		descripcion = request.POST.get('descripcion')

		convocatoria = Convocatoria.objects.get(id=convocatoria_id)

		desafio = Desafio(titulo=titulo, descripcion=descripcion, convocatoria=convocatoria)
		desafio.convocatoria = convocatoria
		desafio.save()

		#desafios = Desafio.objects.all().values('id', 'titulo','descripcion')

		#response=serializers.serialize('json', desafios, fields=('titulo'))

		#return JsonResponse({'results': list(Desafio.objects.filter(id=desafio.id).values('id', 'titulo', 'descripcion'))})
		return HttpResponseRedirect(reverse('desafio:desafio_view', args=(desafio.id,)))


	else:

		return render(request, 'desafio/desafio_new.html', {})


def desafio_view(request, desafio_id):
	
	desafio = Desafio.objects.get(id=desafio_id)
	documentos = Documento.objects.filter(desafio=desafio)


	return render(request, 'desafio/desafio_view.html', {'desafio': desafio, 'documentos': documentos})

	#return JsonResponse({'results': list(Desafio.objects.get(id=desafio_id).values('id', 'titulo', 'descripcion'))})


def upload_documento(request):
	
	if request.method == "POST":
		form = UploadDocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			instance = Documento(documento=request.FILES['documento'])
			instance.save()
			return HttpResponseRedirect('/desafio/desafio_view/')

	else:
		form = UploadDocumentoForm()

	return render(request, 'desafio/desafio_view.html', {'form': form})


