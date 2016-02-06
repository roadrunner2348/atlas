from django.conf.urls import include, url
from .views import *

app_name = "knowledgebase"
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^new_article$', create_article, name="create_article"),
    url(r'^(?P<article_id>[0-9]+)/$', article_detail, name="article_detail"),
    url(r'^(?P<article_id>[0-9]+)/edit$', edit_article, name="edit_article"),
    url(r'^(?P<pk>[0-9]+)/delete/', ArticleDelete.as_view(), name="article_delete"),
    url(r'^search/$', article_search, name="article_search"),
    url(r'^new_tag$', TagCreate.as_view(), name="create_tag"),
    url(r'^tags/(?P<pk>[0-9]+)/$', TagDetail.as_view(), name="tag_detail"),
    url(r'^tags/(?P<pk>[0-9]+)/delete/', TagDelete.as_view(), name="tag_delete"),
    url(r'^tags/(?P<pk>[0-9]+)/edit/', TagUpdate.as_view(), name="tag_update"),
]
