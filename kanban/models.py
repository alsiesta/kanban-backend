from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):        
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    STATUS_CHOICES = [
        ('T', 'To Do'),
        ('I', 'In Progress'),
        ('D', 'Done'),
    ]

    COLOR_CHOICES = [
        ('G', 'Green'),
        ('Y', 'Yellow'),
        ('R', 'Red'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, default='')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L', blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='T', blank=True)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, default='G', blank=True)
    subtask = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0, blank=True)