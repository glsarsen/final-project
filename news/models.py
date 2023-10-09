from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey("Author", related_name="articles", on_delete=models.CASCADE)
    publication_date = models.DateTimeField()
    tags = models.CharField(max_length=400)
    content = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateTimeField()

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey("Article", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.SET_NULL, null=True)

class Bookmark(models.Model):
    article = models.ForeignKey("Article", related_name="bookmarks", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="bookmarks", on_delete=models.CASCADE, default=None)