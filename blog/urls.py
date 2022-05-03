from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.get_posts),
    path('posts/<str:slug>', views.get_post),
]
