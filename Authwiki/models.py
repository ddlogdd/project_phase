from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# Authwiki/models.py

class CustomUser(AbstractUser):
    pass
'''
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.Authwiki', on_delete=models.CASCADE,)
    body = models.TextField()
    def __str__(self):
        return self.title

'''

'''
class Comment(models.Model): # new
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    author = models.ForeignKey(
    get_user_model(), on_delete=models.CASCADE,)
    def __str__(self):
    return self.comment
    def get_absolute_url(self):
    return reverse('article_list')
'''