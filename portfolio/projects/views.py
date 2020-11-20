from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project
from blog.models import Article
# Create your views here.

class ProjectsPage(ListView):
    template_name = 'project.html'
    context_object_name = 'projects'
    model = Project

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()[:5]

        return context
    

class ProjectDetailPage(DetailView):
    template_name = 'project-single.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()[:5]

        return context



