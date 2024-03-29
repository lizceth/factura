from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='usuarios/ingresar.html')),

    # Examples:
    # url(r'^$', 'Factura.views.home', name='home'),
    # url(r'^Factura/', include('Factura.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    #url(r'^/$', 'usuarios.views.login_view'),
    url(r'^ingresar/$','usuarios.views.ingresar'),
    url(r'^privado/$','usuarios.views.privado'),
    url(r'^cerrar/$','usuarios.views.cerrar'),
)

# Uncomment the next line to serve media files in dev.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
