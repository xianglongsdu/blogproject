from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from comments.forms import CommentForm
import markdown

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 1

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
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)

        return context
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        post.body = markdown.markdown(post.body, extensions={'markdown.extensions.extra','markdown.extensions.codehilite', 'markdown.extensions.toc'})
        return post

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False

        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number+2]
        
        if right[-1] < total_pages - 1:
            right_has_more = True
        
        if right[-1] < total_pages:
            last = True
        
        elif page_number == total_pages:
            left = page_range[total_pages-2 if (total_pages-2) > 0 else 0: page_number]
        
            if left[0] > 2:
                left_has_more = True
            
            if left[0] > 1:
                first = True
        
        else:
            right = page_range[page_number:page_number+2]
            left = page_range[total_pages-2 if (total_pages-2) > 0 else 0: page_number]

            if right[-1] < total_pages - 1:
                right_has_more = True
        
            if right[-1] < total_pages:
                last = True
            
            if left[0] > 2:
                left_has_more = True
            
            if left[0] > 1:
                first = True
        
        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data

class ArchivesView(IndexView):
    def get_queryset(self):
        return Post.objects.filter(created_time__year=self.kwargs.get('year'), created_time__month=self.kwargs.get('month')).order_by('-created_time')


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)
    
class TagView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)

