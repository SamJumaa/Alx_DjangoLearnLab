from relationship_app.models import Author, Book, Library, Librarian

# 1) Query all books by a specific author (ForeignKey)
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print(list(books_by_author.values_list("title", flat=True)))

# 2) List all books in a library (ManyToMany)
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print(list(library_books.values_list("title", flat=True)))

# 3) Retrieve the librarian for a library (OneToOne)
librarian = Librarian.objects.get(library=library)
print(librarian.name)
