from django.conf.urls import url
from . import views

app_name = 'JSSLabelWriter'

urlpatterns = [
    url(r'^$', views.device_search_form, name = 'index'),
    url(r'^(?P<device_id>[0-9]+)/$', views.label, name='label'),
    url(r'^printer-instructions$', views.printer_instructions, name="printer-instructions"),
]
