
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
