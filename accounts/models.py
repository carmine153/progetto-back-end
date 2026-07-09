from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('standard', 'Standard User'),
        ('manager', 'Manager/Organizer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='standard')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
    )
    def __str__(self):
        return self.username

# Create your models here.
