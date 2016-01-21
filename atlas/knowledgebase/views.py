from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Tag

# Create your views here.
def index(request):
    tags = Tag.objects.all().order_by("name")
    recently_modified = Article.objects.all().order_by('-date_modified')[:5]
    return render(request, 'knowledgebase/index.html', {'tags':tags, 'recently_modified':recently_modified })
