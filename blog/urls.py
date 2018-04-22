from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path('^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path('^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag')
    
]