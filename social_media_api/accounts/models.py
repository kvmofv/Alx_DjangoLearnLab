from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=255)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField("self", related_name='following', symmetrical=False, blank=True)
