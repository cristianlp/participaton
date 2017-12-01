from django.conf.urls import url

from .views import desafio_new, get_desafios, desafio_view

urlpatterns = [
    url(r'^new$', desafio_new, name='desafio_new'),
    url(r'^view/(?P<desafio_id>\d+)$', desafio_view, name='desafio_view'),
    url(r'^all/(?P<convocatoria_id>\d+)$', get_desafios, name='get_desafios'),
    #url(r'^documento/new$', documento_new, name='documento_new'),
]