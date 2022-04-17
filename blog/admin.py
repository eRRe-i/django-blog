from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'author', 'created', 'published')
    date_hierarchy = 'published'
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
