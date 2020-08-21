from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published')
    list_filter = ('published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = { 'slug': ('title',) }
    date_hierarchy = 'published'
    ordering = ('published',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')