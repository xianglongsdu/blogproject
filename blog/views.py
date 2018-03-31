from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category
from comments.forms import CommentForm
import markdown

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comment_list'] = self.object.comment_set.all()
        return context
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body, extensions={'markdown.extensions.extra','markdown.extensions.codehilite', 'markdown.extensions.toc'})
        return post


class ArchivesView(IndexView):
    def get_queryset(self):
        return Post.objects.filter(created_time__year=self.kwargs.get('year'), created_time__month=self.kwargs.get('month')).order_by('-created_time')


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)
    

