from django.forms import ModelForm
from .models import Article, Tag

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields = ['title', 'body', 'tags']

class TagForm(ModelForm):
    class Meta:
        model=Tag
        fields = ['name']
