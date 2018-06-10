from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
import markdown

def index(request):
    posts = Post.objects.all().order_by('-time')
    categories = Category.objects.all()
    latest = Post.objects.all()[:5]
    dates = Post.objects.dates('time', 'month', 'DESC')
    return render(request, 'blog/index.html', context = {'posts': posts, 'categories': categories, 'latest': latest, 'dates': dates})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.content = markdown.markdown(post.content, extensions = [
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc'
                                    ])
    return render(request, 'blog/detail.html', context={'post': post})

def category(request, category_id):
    posts = Post.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    latest = Post.objects.all()[:5]
    dates = Post.objects.dates('time', 'month', 'DESC')
    return render(request, 'blog/index.html', context = {'posts': posts, 'categories': categories, 'latest': latest, 'dates': dates})

def archive(request, year, month):
    posts = Post.objects.filter(time__year = year, time__month = month)
    categories = Category.objects.all()
    latest = Post.objects.all()[:5]
    dates = Post.objects.dates('time', 'month', 'DESC')
    return render(request, 'blog/index.html', context = {'posts': posts, 'categories': categories, 'latest': latest, 'dates': dates})