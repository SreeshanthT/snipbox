from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    tags = models.ManyToManyField(Tag, related_name="snippets")

    def __str__(self):
        return self.title
