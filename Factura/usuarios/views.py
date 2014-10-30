from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import logout, authenticate, login
#decorador de vigilancia de login

@watch_login
def login_view(request):
    #funcion que permite uniciar sesion en el proyecto django
    #para salir
    logout(request)
    username=password=''
    login_failed=False

    if request.POST:
        username=request.POST['username'].replace('  ','').lower()
        password=request.POST['password']
        user=authenticate(username=my_username, password=my_password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin/')
        else:
            login_failed=True

    return render_to_response('usuarios/login.html',
                              {'login_failed':login_failed},
                              context_instance=RequestContext(request))
