from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, TemplateView, DetailView

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
            'highlighted_article': Article.objects.order_by('view_count').last(),
            'projects' : Project.objects.all()
        }

        return context



class AboutUsPage(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()[:5]

        return context



class ContactPage(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles'] = Article.objects.all()[:5]

        return context