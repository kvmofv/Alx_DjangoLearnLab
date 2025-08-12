from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='kvmofv', password='12345')
        self.client.force_authenticate(user=self.user)

        # Create a sample book and author
        self.author = Author.objects.create(name='Author 1')

        self.book = Book.objects.create(
            title='Book 1',
            publication_year= 2015,
            author = self.author
        )

        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book.id}/'
        self.create_url = '/api/books/create/'
        self.update_url = f'/api/books/update/{self.book.id}/'
        self.delete_url = f'/api/books/delete/{self.book.id}/'

    # --- CRUD TESTS (Authenticated) ---

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2015,
            'author': self.author.id,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.data["title"], "New Book")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'publication_year': self.book.publication_year,
            'author': self.author.id,
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # --- AUTHENTICATION / PERMISSION TESTS ---

    def test_login_and_create_book(self):
        logged_in = self.client.login(username='kvmofv', password='12345')
        self.assertTrue(logged_in)  # Make sure login succeeded

        data = {
            "title": "Book Created After Login",
            "author": self.author.id,
            "publication_year": 2016
        }

        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Book Created After Login")


    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        data = {
            'title': 'Unauth Book',
            'publication_year': 2000,
            'author': self.author.id,
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user_cannot_update_book(self):
        self.client.logout()
        data = {
            'title': 'Hacked Book',
            'publication_year': 2001,
            'author': self.author.id,
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user_cannot_delete_book(self):
        self.client.logout()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
