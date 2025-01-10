from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import datetime

#custom user model,
class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


#Task model
class Task(models.Model):
    STATUS_CHOICES =[
        ('pending','PENDING'),
        ('completed','COMPLETED')
    ]

    PRIORITY_CHOICES = [
        ('low','LOW'),
        ('medium','MEDIUM'),
        ('high','HIGH'),
    ] 

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True) #time for task completion

    def clean(self):
        #date must be in the future
        if self.due_date and self.due_date <= datetime.now():
            raise ValidationError("Due date must be in future.")
        
    def save(self, *args, **kwargs):
        if self.status == 'completed' and not self.completed_at:
            self.completed_at = datetime.now()  # Add timestamp when marked completed
        if self.status == 'pending':
            self.completed_at = None  # Clear timestamp if reverted to pending
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:50]
    
    