from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from . models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('title', 'content', 'author')
    success_message = "%(field)s criado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ('title', 'content')
    success_message = "%(field)s alterado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')

    success_message = "Postagem deletada com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)

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
