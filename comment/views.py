from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm
from .models import Comment
from datetime import datetime 
from django.views.generic import ListView

def post_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment()
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.url = form.cleaned_data['url']
            comment.content = form.cleaned_data['content']
            comment.time = datetime.now()
            comment.save()

            return HttpResponseRedirect('')
    else:
        form = CommentForm()
        return render(request, 'blog/detail.html', context={'form': form})






