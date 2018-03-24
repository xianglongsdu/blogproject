from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]