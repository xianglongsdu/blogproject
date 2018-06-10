from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('post/(?P<post_id>[0-9]+)/', views.detail, name='detail'),
    re_path('category/(?P<category_id>[0-9]+)/', views.category, name='category'),
    re_path('archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archive, name='archive'),
]