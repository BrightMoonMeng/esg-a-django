from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models


# post model
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        f"[{self.pk}] {self.title}"
        return str(self.pk) + self.title