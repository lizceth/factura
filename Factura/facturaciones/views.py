from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from asistentes.models import Persona, Participante
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from asistentes.forms import PersonaForm, ParticipanteForm


def clienteList(request):
    clientes=Cliente.objects.all().order_by('id')
    return render(request, 'clientes/clienteList.html', 'clientes':clientes)

def clienteAdd(request):
    if request.method=='POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('clienteList')
        else:
            formulario=ClienteForm()
        return render_to_response('facturaciones/clienteAdd.html',
                                  {'formulario':formulario},
                                  context_instance=RequestContext(request))


def productoAdd(request):
    if request.method=='POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('productoList')
        else:
            formulario=ClienteForm()
        return render_to_response('facturaciones/productoAdd.html',
                                  {'formulario':formulario},
                                  context_instance=RequestContext(request))

def detalle(request):
    pass
