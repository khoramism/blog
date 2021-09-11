# my_app/urls.py

from django.urls import path,re_path
from . import views

app_name = 'blog'


urlpatterns = [
    re_path(r'(?P<slug>[-\w]+)/', views.detail, name='detail'),
    path('', views.list_view, name='list')
]
