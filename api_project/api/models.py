"""This file contains the nodels for the api app."""
from django.db import models

# Create your models here.

class Book(models.Model):
    """This is the model for the book."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)

