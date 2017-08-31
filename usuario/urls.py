from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [

    url(r'^login/$', views.usuario_login, name='login'),
    url(r'^logout/$', views.usuario_logout, name='logout'),

]
