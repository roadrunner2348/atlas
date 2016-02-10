from django.conf.urls import include, url
from .views import *

app_name = "inventory"
urlpatterns = [
    #Program URLS
    url(r'^programs/$', ProgramIndex.as_view(), name="program_index"),
    url(r'^programs/new/$', ProgramCreate.as_view(), name="program_create"),
    url(r'^programs/(?P<pk>[0-9]+)/$', ProgramDetailView.as_view(), name="program_detail"),
    url(r'^programs/(?P<pk>[0-9]+)/edit$', ProgramUpdate.as_view(), name="program_update"),
    url(r'^programs/(?P<pk>[0-9]+)/delete$', ProgramDelete.as_view(), name="program_delete"),
    #Client URLS
    url(r'^clients/$', ClientIndex.as_view(), name="client_index"),
    url(r'^clients/new/$', ClientCreate.as_view(), name="client_create"),
    url(r'^clients/(?P<pk>[0-9]+)/$', ClientDetailView.as_view(), name="client_detail"),
    url(r'^clients/(?P<pk>[0-9]+)/edit$', ClientUpdate.as_view(), name="client_update"),
    url(r'^clients/(?P<pk>[0-9]+)/delete$', ClientDelete.as_view(), name="client_delete"),
]
