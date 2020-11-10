from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home-page"),
    path('about/', views.AboutUsPage.as_view(), name="about-page"),
    path('contact/', views.ContactPage.as_view(), name="contact-page")
]