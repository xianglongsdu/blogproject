from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
