# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from timezone_field import TimeZoneField


class Usuarios(models.Model):
    """
    Modelo para almacenar la configuración y preferencias de usuarios
    adicionales.
    Extiende el modelo user.
    """

    user = models.OneToOneField(User, related_name='settings')
    codigo=models.CharField(max_length=5, unique=True)
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    fecha_nacimiento=models.DateTimeField()


    def username(self):
        return self.user.username
    username.admin_order_field = 'user__username'

    class Meta:
        verbose_name_plural = 'Configuraciones de usuario'
