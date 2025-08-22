from rest_framework import serializers
from . models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ["author", "title", "content", "created_at", "updated_at"]

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ["post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author", "post", "created_at", "updated_at"]