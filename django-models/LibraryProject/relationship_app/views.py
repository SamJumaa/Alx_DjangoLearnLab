from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


def list_books(request):
    books = Book.objects.select_related("author").all()
    lines = [f"{b.title} by {b.author.name}" for b in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # optional template
    context_object_name = "library"


