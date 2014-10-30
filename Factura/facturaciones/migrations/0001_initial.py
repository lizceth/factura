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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ruc', models.CharField(max_length=11)),
                ('razon_social', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('importe', models.FloatField()),
                ('igv', models.FloatField()),
                ('base_imponible', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.CharField(max_length=3)),
                ('numero', models.CharField(unique=True, max_length=6)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('igv_total', models.FloatField()),
                ('total', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('cliente', models.ForeignKey(to='facturaciones.Cliente')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('precio_unit', models.FloatField()),
                ('categoria', models.CharField(max_length=1, choices=[(b'A', b'afecto'), (b'I', b'inafecto')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(to='facturaciones.Producto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle',
            name='registro',
            field=models.ForeignKey(to='facturaciones.Factura'),
            preserve_default=True,
        ),
    ]
