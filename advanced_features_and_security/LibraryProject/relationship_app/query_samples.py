import os  
import django  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()  

from relationship_app.models import Author, Book, Library, Librarian  

author_name = 'F. Scott Fitzgerald'
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)


library_name = 'Maddison'

library = Library.objects.get(name=library_name)
books = library.books.all()

library_name = 'Maddison'
library = Library.objects.get(name=library_name)

librarian = Librarian.objects.get(library=library)

