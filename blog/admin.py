from django.contrib import admin
from .models import Post, Category
# Register your models here.


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'published')
    list_filter = ('name', 'created', 'published')
    date_hierarchy = 'published'
    search_fields = ('name', )



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'status')
    list_filter = ('status', 'author', 'created', 'published')
    date_hierarchy = 'published'
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
