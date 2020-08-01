from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField (max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField (max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField (max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title