from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
