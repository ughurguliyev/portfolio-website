from django.shortcuts import render
from django.views.generic import ListView

from .models import Project

# Create your views here.

class ProjectsPage(ListView):
    template_name = 'project.html'
    context_object_name = 'projects'
    model = Project



