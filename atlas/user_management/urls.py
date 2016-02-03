from django.conf.urls import url
from . import views

app_name = "user_management"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<user_id>[0-9]+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<user_id>[0-9]+)/change_status/$', views.change_status, name="change_status"),
    url(r'^(?P<user_id>[0-9]+)/delete/$', views.delete, name="delete"),
    url(r'^create/$', views.create, name = 'create'),
    url(r'^update_password$',
        'django.contrib.auth.views.password_change',
        name='update_password',
        kwargs={
            'template_name':'user_management/update_password.html',
            'post_change_redirect':'user_management:update_password_done',
        }
    ),
    url(r'^update_password_done$',
        'django.contrib.auth.views.password_change_done',
        name='update_password_done',
        kwargs={'template_name':'user_management/update_password_done.html'}
    ),


]
