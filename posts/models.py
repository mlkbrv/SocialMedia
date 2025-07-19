from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    caption = models.TextField()
    image = models.ImageField(upload_to='posts/',blank=True,null=True)
    slug = models.SlugField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='posts_liked', blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)