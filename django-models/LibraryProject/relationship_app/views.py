from django.shortcuts import render
from django.views.generic import DetailView
from . models import Book, Library

def list_books(request):
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

class LibraryDetailview(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    