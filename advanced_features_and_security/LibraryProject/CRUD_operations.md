# CRUD Operations Using Django Shell

```python
# =========================
# CREATE
# =========================
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
# Output:
# <Book: 1984>


# =========================
# RETRIEVE
# =========================
book.id, book.title, book.author, book.publication_year
# Output:
# (1, '1984', 'George Orwell', 1949)


# =========================
# UPDATE
# =========================
book.title = "Nineteen Eighty-Four"
book.save()

book.id, book.title, book.author, book.publication_year
# Output:
# (1, 'Nineteen Eighty-Four', 'George Orwell', 1949)


# =========================
# DELETE
# =========================
book.delete()
# Output:
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output:
# <QuerySet []>


