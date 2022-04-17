from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name", )

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(verbose_name="Título", max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="get_posts")
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    content = models.TextField(verbose_name="Conteúdo")
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


@receiver(post_save, sender=Post)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        return instance.save()

# Create your models here.
