from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
import markdown
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
    comment_list = post.comment_set.all()
    form = CommentForm()

    return render(request, 'blog/detail.html', context={'post': post, 'comment_list': comment_list, 'form': form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.increase_views()
        post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
        return post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = self.object.comment_set.all()
        context['form'] = CommentForm()
        return context

class ArchivesView(IndexView):
    def get_queryset(self):
        return Post.objects.filter(created_time__year=self.kwargs['year'], created_time__month=self.kwargs['month'])

class CategoryView(IndexView):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'])
