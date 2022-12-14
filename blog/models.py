from pyexpat import model
from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField('Categoría', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Post(models.Model):
    imagen = models.ImageField(upload_to='images/')
    title = models.CharField('Título', max_length=200)
    summary = models.TextField(blank=True, max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    views_number = models.IntegerField(default=0, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.content[:10]
