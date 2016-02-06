from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'pk': self.pk})

    def delete(self, *args, **kwargs):
        """
        Override default model method so articles are not deleted when a tag is removed
        """
        self.article_set.clear()
        super(Tag, self, *args, **kwargs).delete()

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

    def delete(self, *args, **kwargs):
        """
        Override default model method so tags are not deleted when a article is removed
        """
        self.tags.clear()
        super(Article, self, *args, **kwargs).delete()
