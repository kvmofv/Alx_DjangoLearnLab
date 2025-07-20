import os  
import django  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()  

from relationship_app.models import Author, Book, Library, Librarian  

books = Book.objects.filter(author__name='F. Scott Fitzgerald')

library = Library.objects.get(name='Maddison')
books = library.books.all()

library = Library.objects.get(name='Maddison')
librarian = library.librarian  
