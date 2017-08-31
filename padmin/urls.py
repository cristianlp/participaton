from django.conf.urls import url

from .views import HomeView, ConvocatoriaNuevoP1View, ConvocatoriaNuevoP2View, ConvocatoriaDetailView, ConvocatoriaEditView

urlpatterns = [

	url(r'^convocatoria/new/1/$', ConvocatoriaNuevoP1View.as_view(), name="convocatoria_new_p1"),
	url(r'^convocatoria/new/2/$', ConvocatoriaNuevoP2View.as_view(), name="convocatoria_new_p2"),
	url(r'^convocatoria/view/(?P<pk>\d+)$', ConvocatoriaDetailView.as_view(), name='convocatoria_detail'),
	url(r'^convocatoria/edit/(?P<pk>\d+)$', ConvocatoriaEditView.as_view(), name='convocatoria_edit'),

    url(r'^$', HomeView.as_view(), name="home"),

]