from django.views.generic import ListView
from django.db.models import Prefetch
from django.shortcuts import render
from articles.models import Article, Scope, ArticleInScope


def articles_list(request):
    template = 'articles/news.html'

    qs = ArticleInScope.objects.select_related('topic').order_by('-is_main')
    object_list = Article.objects.all().prefetch_related(Prefetch('scopes', queryset=qs)).order_by('-published_at').all()

    for article in object_list:
        for scope in article.scopes.all():
            print(scope.topic)
    context = {
        'object_list': object_list,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
