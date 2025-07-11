```python
# Create a Book instance
>>> book1 = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book1.save()
# Output: saves successfully, no visible output



---

###  `retrieve.md`
```markdown
```python
# Retrieve all Book instances
>>> Book.objects.all()
# Output:
<QuerySet [<Book: Book object (1)>]>

# Retrieve first book details
>>> book = Book.objects.first()
>>> book.title
# Output: '1984'
>>> book.author
# Output: 'George Orwell'
>>> book.publication_year
# Output: 1949



---

###  `update.md`
```markdown
```python
# Update the title
>>> book = Book.objects.first()
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
# Output: 'Nineteen Eighty-Four'



---

###  `delete.md`
```markdown
```python
# Delete the book
>>> book = Book.objects.first()
>>> book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
>>> Book.objects.all()
# Output: <QuerySet []>
