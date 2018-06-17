from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from comment.forms import CommentForm
from comment.models import Comment
import markdown

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['latest'] = Post.objects.order_by('-time')[:5]
        context['dates'] = Post.objects.dates('time', 'month', 'DESC')
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        comments = Comment.objects.filter(post__pk = self.kwargs['pk']).order_by('-time')
        context['comments'] = comments
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        md = markdown.Markdown(extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        post.content = md.convert(post.content)
        post.toc = md.toc
        
        context['post'] = post
        return context

    def get_object(self):
        object = super().get_object()
        object.count += 1
        object.save()
        return object


class CategoryView(IndexView):
    def get_queryset(self, **kwargs):
        posts = Post.objects.filter(category_id = self.kwargs['category_id'])
        return posts

class ArchiveView(IndexView):
    def get_queryset(self, **kwargs):
        posts = Post.objects.filter(time__year = self.kwargs['year'], time__month = self.kwargs['month'])
        return posts
