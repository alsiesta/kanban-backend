from email.mime import image
from re import sub
from django.db import models
from django.utils import timezone
from django.conf import settings


class HomeContent(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    imgcaption = models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(default=timezone.now),
    image = models.ImageField(upload_to='img/', default='', blank=True)
    
    def __str__(self):
        return f'({self.id})  {self.title}'