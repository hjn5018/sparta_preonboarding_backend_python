from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    
class Role(models.Model):
    role = models.CharField(max_length=20, default='USER', unique=True)

    def __str__(self):
        return self.role

class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE)