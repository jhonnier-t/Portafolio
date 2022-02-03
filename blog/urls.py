from importlib.resources import path
from unicodedata import name
from django import views
from django.urls import path
from .views import render_post, post_detail

app_name = 'blog'

urlpatterns = [
    path('', render_post, name='posts'),
    path('<int:post_id>', post_detail, name="post_detail")
]

