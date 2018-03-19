from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    fieldsets = (('基本项目', {'fields':('title', 'excerpt', 'body')}), ('高级项目', {'classes': ('collapse',), 'fields': ('category', 'created_time')}))
    list_display = ['title', 'author', 'category', 'created_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
