from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from .models import Article, Tag
from .forms import ArticleForm, TagForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class TagCreate(CreateView):
    model = Tag
    fields = ['name']

    def get_success_url(self):
        return reverse('knowledgebase:index')

@method_decorator(login_required, name='dispatch')
class TagDetail(DetailView):
    model = Tag

@login_required
def index(request):
    tags = Tag.objects.all().order_by("name")
    article_list = Article.objects.all().order_by('-date_modified')[:5]
    tag_form = TagForm()
    return render(request, 'knowledgebase/index.html', {'tags':tags, 'article_list':article_list, 'form':tag_form })

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('/kb/' + str(article.id))
        else:
            return render(request, 'knowledgebase/article_form.html', {'form':form})
    else:
        form = ArticleForm()
        return render(request, 'knowledgebase/article_form.html', {'form':form})

@login_required
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

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'knowledgebase/article_detail.html', {'article':article})
