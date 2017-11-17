from django.conf.urls import url

from .views import HomeView, ConvocatoriaNuevoView, ConvocatoriaDetailView, ConvocatoriaEditView, convocatoria_publicar, convocatoria_desafios

urlpatterns = [

	url(r'^convocatoria/new/$', ConvocatoriaNuevoView.as_view(), name="convocatoria_new"),
	url(r'^convocatoria/view/(?P<pk>\d+)$', ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
	url(r'^convocatoria/edit/(?P<pk>\d+)$', ConvocatoriaEditView.as_view(), name='convocatoria_edit'),
	url(r'^convocatoria/publicar/(?P<convocatoria_id>\d+)$', convocatoria_publicar, name='convocatoria_publicar'),
	url(r'^convocatoria/desafios/(?P<convocatoria_id>\d+)$', convocatoria_desafios, name='convocatoria_desafios'),

    url(r'^$', HomeView.as_view(), name="home"),

]