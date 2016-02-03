from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, Tag
from .forms import ArticleForm

# Create your views here.
def index(request):
    tags = Tag.objects.all().order_by("name")
    recently_modified = Article.objects.all().order_by('-date_modified')[:5]
    return render(request, 'knowledgebase/index.html', {'tags':tags, 'recently_modified':recently_modified })

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=false)
            author = request.user.first_name + " " + request.user.last_name
            article.author = author
            article.save()
            return redirect('/kb/' + str(article.id))
        else:
            return render(request, 'knowledgebase/article_form.html', {'form':form})
    else:
        form = ArticleForm()
        return render(request, 'knowledgebase/article_form.html', {'form':form})

def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    edit = True
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/kb/' + str(article_id))
        else:
            return render(request, 'knowledgebase/article_form.html', {'form':form, 'article':article, 'edit':edit })
    else:
        form = ArticleForm(instance=article)
        return render(request, 'knowledgebase/article_form.html', {'form':form, 'article':article, 'edit':edit })

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'knowledgebase/article_detail.html', {'article':article})
