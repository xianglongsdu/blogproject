from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from . import views
from .views import IndexView, PostDetailView, CategoryView, ArchiveView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path('post/(?P<pk>[0-9]+)/', PostDetailView.as_view(), name='detail'),
    re_path('category/(?P<category_id>[0-9]+)/', CategoryView.as_view(), name='category'),
    re_path('archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', ArchiveView.as_view(), name='archive'),
]