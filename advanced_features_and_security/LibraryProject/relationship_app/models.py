"""Models for managing relationships in the relationship_app."""
from django.db import models
from django.conf import settings
user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Author(models.Model):
    """Represents an author who can write one or more books."""

    name=models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Book(models.Model):
    """Represents a book written by an author."""
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)


    class Meta:
        """Metadata options for the Author model, including permissions."""
        permissions = (
            ("can_add_book", "Can add book (custom)"),
            ("can_change_book", "Can change book (custom)"),
            ("can_delete_book", "Can delete book (custom)"),
        )

    def __str__(self) -> str:
        return str(self.title)


class Library(models.Model):
    """Represents a library that can have multiple books and a librarian. """
    name=models.CharField(max_length=255)
    books=models.ManyToManyField(Book)

    def __str__(self):
        return str(self.name)


class Librarian(models.Model):
    """Represents a librarian who manages a library."""
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)



#UserProfile and role choices
class UserProfile(models.Model):
    """Represents a user profile with a role )admin, librarian, member) linked to a user. """
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user} - {self.role}"
