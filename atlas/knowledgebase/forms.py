from django.forms import ModelForm
from .models import Article, Tag

class ArticleForm(ModelForm):
    class Meta:
        model=Article
        fields = ['title', 'body', 'tags']
