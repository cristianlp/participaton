from django.db import models

from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True)
    imagen = models.ImageField(upload_to="imagenes", blank=True)

    def __str__(self):
        return self.user.username

