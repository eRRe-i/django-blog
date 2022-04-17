from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('title', 'slug', 'content', 'author')


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ('title', 'content')


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')


#     title = models.CharField(max_length=250)
#     slug = models.SlugField(max_length=250)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     content = models.TextField()
#     published = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     altered = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10,
#                               choices=STATUS,
#                               default='draft')
