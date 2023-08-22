from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.username
