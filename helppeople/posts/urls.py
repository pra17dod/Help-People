from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin')
]
