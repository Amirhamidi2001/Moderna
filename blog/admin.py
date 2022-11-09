from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    """This class """
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status')
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


class CommentAdmin(admin.ModelAdmin):
    """This class is for """
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']


admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
