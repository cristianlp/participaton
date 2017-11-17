from django.conf.urls import url

from .views import desafio_new, get_desafios

urlpatterns = [
    url(r'^new$', desafio_new, name='desafio_new'),
    url(r'^all/(?P<convocatoria_id>\d+)$', get_desafios, name='get_desafios')
]