"""This module defines the modules for the bookshelf app."""
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom user manager to handle user creations."""

    def create_user(self, username, password=None, **extra_fields):
        """creates a user with the given username and passwords."""

        if not username:
            raise ValueError("The username must be set")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """creates a superuser with the given username and passwords."""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    """customer user model that extends the default Django user model with additional fields."""
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return str(self.username)



# Create your models here.
class Book (models.Model) :
    """Represents a book in the bookshelf app."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
