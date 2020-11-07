from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectsPage.as_view(), name='projects-page')
]