from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer

# Allows unauthenticated users to view the list of books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

# Allows unauthenticated users to retrieve a specific book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# Requires authentication to create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom validation hook to prevent empty titles
    def perform_create(self, serializer):
        title = self.request.data.get('title')
        if not title:
            raise ValidationError('Title cannot be empty')
        serializer.save()

# Requires authentication to update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom validation hook to prevent empty titles
    def perform_update(self, serializer):
        title = self.request.data.get('title')
        if not title:
            raise ValidationError('Title cannot be empty')
        serializer.save()

# Requires authentication to delete a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]