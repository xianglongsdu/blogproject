from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-time')
    return render(request, 'blog/index.html', context = {'posts': posts})
