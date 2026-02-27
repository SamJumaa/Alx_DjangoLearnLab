from rest_framework import generics,viewsets
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    """API view to retrieve a list of all books."""

    queryset = Book.objects.all() #type: ignore
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet providing CRUD operations for Book."""

    queryset = Book.objects.all() #type: ignore
    serializer_class = BookSerializer
