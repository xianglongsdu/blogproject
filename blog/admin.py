from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'excerpt', 'content','author', 'time'),
        }),
        ('高级选项', {
            'classes': ('collapse',),
            'fields': ('category', 'tags')
        })
    )
    list_display = ('title', 'excerpt', 'author', 'time')
    list_display_links = ('title', 'excerpt')
    list_editable = ('author', 'time')
    list_filter = ('category', 'tags')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
