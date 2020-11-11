from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesPage.as_view(), name="articles-page"),
]