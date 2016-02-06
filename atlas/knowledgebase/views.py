from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from .models import Article, Tag
from .forms import ArticleForm, TagForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q


@method_decorator(login_required, name='dispatch')
class TagCreate(CreateView):
    model = Tag
    fields = ['name']

    def get_success_url(self):
        return reverse('knowledgebase:index')

@method_decorator(login_required, name='dispatch')
class TagDetail(DetailView):
    model = Tag

@method_decorator(login_required, name='dispatch')
class TagDelete(DeleteView):
    model = Tag

    success_url = reverse_lazy('knowledgebase:index')

@method_decorator(login_required, name='dispatch')
class TagUpdate(UpdateView):
    model = Tag
    fields = ['name']
    success_url = reverse_lazy('knowledgebase:index')

@method_decorator(login_required, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('knowledgebase:index')

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
            article = form.save(commit=False)
            article.author = request.user.first_name + " " + request.user.last_name
            article.save()
            form.save_m2m()
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

def article_search(request):
    """Get search string from POST data"""
    search_string = request.POST['search_string']
    """Creat Q objects for database query"""
    query = Q(title__icontains=search_string)|Q(body__icontains=search_string)
    """Get results of query and assign to search_results variable"""
    search_results = Article.objects.filter(query)
    """render search results page, include search_string & search_results in the context data"""
    return render(request, 'knowledgebase/search_results.html', { 'search_string':search_string, 'article_list':search_results })
