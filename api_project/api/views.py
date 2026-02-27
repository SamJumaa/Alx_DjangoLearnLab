from rest_framework import generics
from api.serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    """API view to retrieve a list of all books."""

    queryset = Book.objects.all()  # type: ignore
    serializer_class = BookSerializer

