from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = SummernoteTextField()
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:home')
