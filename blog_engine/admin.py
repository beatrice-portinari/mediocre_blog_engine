from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'is_published')
    search_fields = ('content', 'title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_on', 'active', 'post', 'body')
    list_filter = ('active', 'created_on')
    search_fields = ('username', 'body', 'post')