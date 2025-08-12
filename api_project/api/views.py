from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    - Uses TokenAuthentication.
    - Only authenticated users can access these endpoints.
    - Supports full CRUD via router.
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes  = [IsAuthenticated]


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    