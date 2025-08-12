from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from relationship_app.forms import BookForm
from .models import Book
from .forms import ExampleForm

def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})


# Views below use @permission_required to enforce custom Book permissions.
# Each view checks:
# - can_create: add_book
# - can_edit: edit_book
# - can_delete: delete_book
# - can_view: list_books
#
# Permissions are assigned to groups:
# - Viewers: can_view
# - Editors: can_create, can_edit
# - Admins: all
#
# Users must be assigned to a group in Django admin to get the permissions.

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {"form": form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
