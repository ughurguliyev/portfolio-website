from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView

from .forms import ContactForm
from blog.models import Article
from projects.models import Project


# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context = {
            'articles' : Article.objects.all()[:3],
            'projects' : Project.objects.all()
        }

        return context


class AboutUsPage(TemplateView):
    template_name = 'about.html'
    
    

class ContactPage(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/projects/'
