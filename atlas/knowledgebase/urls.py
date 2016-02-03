from django.conf.urls import include, url
from . import views

app_name = "knowledgebase"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new_article$', views.create_article, name="create_article"),
    url(r'^(?P<article_id>[0-9]+)/$', views.article_detail, name="article_detail"),
    url(r'^(?P<article_id>[0-9]+)/edit$', views.edit_article, name="edit_article"),

]
