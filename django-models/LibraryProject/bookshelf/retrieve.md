
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

>>> Book.objects.get(title="1984")
# Output: <Book: Book object (1)>
>>> book = Book.objects.get(title="1984")
>>> book.title
# Output: '1984'
>>> book.author
# Output: 'George Orwell'
>>> book.publication_year
# Output: 1949

