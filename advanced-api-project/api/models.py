from django.db import models


class Author(models.Model):
    
    #Represents an author who can write one or more books.
    
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Book(models.Model):
    
    #Represents a book with a title, publication year, and a relationship to an author.
    #Each book is linked to one author via a ForeignKey relationship.

    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title