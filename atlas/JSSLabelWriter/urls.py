from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.device_search_form, name = 'index'),
    url(r'^(?P<device_id>[0-9]+)/$', views.label, name='label'),
]
