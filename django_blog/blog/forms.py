from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']