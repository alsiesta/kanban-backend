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
    due_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    subtask = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)