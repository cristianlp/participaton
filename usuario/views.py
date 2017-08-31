from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse

from django.contrib import messages
from .forms import LoginForm

def usuario_login(request):

    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('ideas:idea_list', args=[]))
        else:
            messages.error(request, "Verifique el usuario y/o contraseña")

    return render(request, "usuarios/login.html", {'form': form})


def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('usuarios:login', args=[]))
