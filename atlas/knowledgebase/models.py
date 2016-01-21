from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField("Article")
