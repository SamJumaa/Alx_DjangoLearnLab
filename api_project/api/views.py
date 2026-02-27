""" Views for the Book API. Provides endpoints for CRUD operations on Book model."""
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView):
    """API view to retrieve a list of all books."""

    queryset = Book.objects.all() #type: ignore
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access this view


class BookViewSet(viewsets.ModelViewSet):
    """ViewSet providing CRUD operations for Book."""

    queryset = Book.objects.all() #type: ignore
    serializer_class = BookSerializer

    def get_permissions(self):
        # Read-only for any authenticated user
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        # Write actions require admin
        return [IsAdminUser()]

