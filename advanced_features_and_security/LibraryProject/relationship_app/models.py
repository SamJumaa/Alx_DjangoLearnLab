from django.db import models
from django.conf import settings


class Author(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)


    class Meta:
        permissions = (
            ("can_add_book", "Can add book (custom)"),
            ("can_change_book", "Can change book (custom)"),
            ("can_delete_book", "Can delete book (custom)"),
        )

    def __str__(self):
        return (self.title)


class Library(models.Model):
    name=models.CharField(max_length=255)
    books=models.ManyToManyField(Book)

    def __str__(self):
        return str(self.name)


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    
#UserProfile and role choices
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user} - {self.role}" 
    
