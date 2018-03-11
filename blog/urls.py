from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    
]