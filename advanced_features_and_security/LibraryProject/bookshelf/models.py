from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be provided.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser')
        
        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(max_length=100, choices=ROLES)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
     
    objects = CustomUserManager()

    def __str__(self):
        return self.username

# This model defines custom permissions:
# - can_view: View books in custom views
# - can_create: Add books in custom views
# - can_edit: Edit books in custom views
# - can_delete: Delete books in custom views
#
# These are enforced in views.py using @permission_required decorators.
# Groups are:
# - Viewers: can_view
# - Editors: can_create, can_edit
# - Admins: all permissions

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view boook"),
            ("can_edit", "Can edit book"),
            ("can_create", "Can create book"),
            ("can_add", "Can add book"),
        ]