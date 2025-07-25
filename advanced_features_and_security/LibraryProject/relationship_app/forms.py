from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book
from bookshelf.models import CustomUser

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=False, widget=forms.SelectDateWidget)
    profile_photo = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role', 'date_of_birth', 'profile_photo')
