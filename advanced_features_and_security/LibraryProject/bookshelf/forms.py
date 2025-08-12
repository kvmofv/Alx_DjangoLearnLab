from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ✅ ExampleForm shows input validation for Book.
    Uses Django's ORM & built-in validators to ensure safe data.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']  # adjust to your Book fields!


# ExampleForm demonstrates secure input handling using Django forms.
