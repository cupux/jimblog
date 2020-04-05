from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogArticle(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"