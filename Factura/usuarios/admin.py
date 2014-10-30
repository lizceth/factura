from django.contrib import admin
from usuarios.models import Usuarios


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'codigo',
        'nombres',
        'apellidos',
        'fecha_nacimiento',
    ]


admin.site.register(Usuarios, UserAdmin)
