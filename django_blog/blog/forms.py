from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment
from taggit.forms import TagWidget

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {'tags': TagWidget(),}

    def clean_field(self):
        tags = self.cleaned_data.get('tags')

        if len(tags) > 5:
            raise forms.ValidationError("You can add a maximum of 5 tags.")

        # Restrict length of each tag
        for tag in tags:
            if len(tag.name) > 20:
                raise forms.ValidationError(f"Tag '{tag}' is too long (max 20 characters).")
        return tags

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_field(self):
        tags = self.cleaned_data.get('tags')

        if len(tags) > 5:
            raise forms.ValidationError("You can add a maximum of 5 tags.")

        # Restrict length of each tag
        for tag in tags:
            if len(tag.name) > 20:
                raise forms.ValidationError(f"Tag '{tag}' is too long (max 20 characters).")
        return tags

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