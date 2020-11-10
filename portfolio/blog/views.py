from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


class ArticlesPage(ListView):
    template_name = 'blog.html'
    model = Article
    context_object_name = 'articles'