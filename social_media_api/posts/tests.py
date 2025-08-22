from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post, Comment

User = get_user_model()

class PostAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

    def test_create_post(self):
        response = self.client.post("/api/posts/", {"title": "Test", "content": "Content"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

    def test_only_owner_can_edit_post(self):
        post = Post.objects.create(title="Owner post", content="data", author=self.user)
        # login with another user
        other_user = User.objects.create_user(username="other", password="12345")
        self.client.login(username="other", password="12345")
        response = self.client.put(f"/api/posts/{post.id}/", {"title": "Hack", "content": "try"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentAPITest(APITestCase):
    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username="user1", password="pass123")
        self.user2 = User.objects.create_user(username="user2", password="pass123")

        # Create a post by user1
        self.post = Post.objects.create(author=self.user1, title="Test Post", content="Post content")

        # Auth token
        self.client.login(username="user1", password="pass123")

    def test_create_comment(self):
        url = f"/api/posts/{self.post.id}/comments/"
        data = {"content": "Nice post!"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

    def test_list_comments(self):
        # Create comments
        Comment.objects.create(author=self.user1, post=self.post, content="First comment")
        Comment.objects.create(author=self.user2, post=self.post, content="Second comment")

        url = f"/api/posts/{self.post.id}/comments/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)  # since pagination is enabled
        
    def test_update_own_comment(self):
        # User1 creates a comment
        comment = Comment.objects.create(author=self.user1, post=self.post, content="Initial comment")

        url = f"/api/posts/{self.post.id}/comments/{comment.id}/"
        data = {"content": "Updated comment"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertEqual(comment.content, "Updated comment")

    def test_delete_other_user_comment_forbidden(self):
        # User1 creates a comment
        comment = Comment.objects.create(author=self.user1, post=self.post, content="User1 comment")

        # Login as User2
        self.client.logout()
        self.client.login(username="user2", password="pass123")

        url = f"/api/posts/{self.post.id}/comments/{comment.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
