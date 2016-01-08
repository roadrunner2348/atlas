from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^test/$', views.jss_device_search, name = 'test'),
]
