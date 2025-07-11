
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
