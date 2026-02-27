""" This file contains the serializers for the api app."""
from rest_framework import serializers
from.models import Book

class BookSerializer(serializers.ModelSerializer):
    """This is the serializer for the book model."""
    class Meta:
        model = Book
        fields = "__all__"
