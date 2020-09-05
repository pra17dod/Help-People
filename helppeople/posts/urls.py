from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('about/', views.about, name = 'about')
]
