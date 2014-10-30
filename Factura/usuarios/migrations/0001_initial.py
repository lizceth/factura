# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=5)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('user', models.OneToOneField(related_name=b'settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Configuraciones de usuario',
            },
            bases=(models.Model,),
        ),
    ]
