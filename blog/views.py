from django.shortcuts import render, get_object_or_404
import markdown
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
    comment_list = post.comment_set.all()
    form = CommentForm()

    return render(request, 'blog/detail.html', context={'post': post, 'comment_list': comment_list, 'form': form})

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    post_list = Post.objects.filter(category_id=pk)
    return render(request, 'blog/index.html', context={'post_list': post_list})