from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Post(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    altered = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='draft')

    objects = models.Manager()
    get_published = PublishedManager()

    class Meta:
        ordering = ('-published', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})

    def get_absolute_url_update(self):
        return reverse('post_update', kwargs={"slug": self.slug})

    def get_absolute_url_delete(self):
        return reverse('post_delete', kwargs={"slug": self.slug})

# Create your models here.