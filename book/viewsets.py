#book/viewsets.py
from rest_framework import viewsets
from book.models import Book
from book.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book