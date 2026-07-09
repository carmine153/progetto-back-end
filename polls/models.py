from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) 
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='polls')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
# Create your models here.
