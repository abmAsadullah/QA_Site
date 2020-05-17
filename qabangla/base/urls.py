from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('article/', views.article, name='article'),
    path('test/', views.test, name='test'),
]