from django.conf.urls  import patterns, url
from django.contrib.auth.views import logout
from .views import login_view

urlpatterns=patterns('',
                     url(regex=r'^login/$', view=login_view, name='login'),
                     url(regex=r'^logout/$',view=logout, kwargs={'next_page':'/usuarios/login/'}, name='logout'),

)
