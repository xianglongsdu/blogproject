from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Comment
from blog.models import Post
from datetime import datetime 
from django.views.generic import ListView

def post_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.url = form.cleaned_data['url']
            comment.content = form.cleaned_data['content']
            comment.time = datetime.now()
            comment.post = Post.objects.get(pk=pk)
            comment.save()

            return HttpResponseRedirect(reverse('blog:detail', kwargs={'pk': pk}))
    else:
        form = CommentForm()
        return render(request, 'blog/detail.html', context={'form': form})






