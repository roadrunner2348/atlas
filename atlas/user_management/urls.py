from django.conf.urls import url
from . import views

app_name = "user_management"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<user_id>[0-9]+)/edit/$', views.edit, name="edit"),
]
