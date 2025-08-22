--------------------|
Project Setup       |
--------------------|

Clone the repository:

git clone https://github.com/kvmofv/Alx_DjangoLearnLab
cd social_media_api

Install dependencies:

- pip install -r requirements.txt


Apply migrations:

- python manage.py migrate

Run the development server:

- python manage.py runserver
----------------------------------------------
User Model Overview

* Custom user model extends AbstractUser.

* Fields include:
- username (unique identifier)
- email (unique, required)
- profile_picture (optional image upload)
- bio (text field for profile info)
- password (hashed, not stored in plain text)

--------------------|
Authentication Flow |
--------------------|
1. Register

Endpoint: POST /api/register/

Request body:

{
  "username": "example_user",
  "email": "user@example.com",
  "password": "securepassword",
  "bio": "Short bio text",
  "profile_picture": "<file>"
}


Response:

{
  "id": 1,
  "username": "example_user",
  "email": "user@example.com"
}

2. Login

Endpoint: POST /api/login/

Request body:

{
  "username": "example_user",
  "password": "securepassword"
}


Response:

{
  "detail": "Login successful"
}

3. Token Retrieval

Endpoint: POST /api/token/

Request body:

{
  "username": "example_user",
  "password": "securepassword"
}


Response:

{
  "token": "abcd1234efgh5678"
}

4. Authenticated Requests

- Add token in the Authorization header: {Authorization: Token abcd1234efgh5678}
------------------------------------
Testing:

How to Run Tests

- Make sure you are inside your Django project root (where manage.py lives).

Run all tests:

- python manage.py test

------------------|
Post API Tests    |
------------------|
Tests implemented:

- Create Post – ensures authenticated users can create posts.
- List Posts – validates retrieval of all posts with pagination.
- Update Own Post – confirms only the author can edit their own posts.
- Delete Other’s Post Forbidden – prevents users from deleting posts they don’t own.

Sample Output (truncated):

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 1.234s

OK

Comment API Tests

Tests implemented:

- Create Comment – verifies that authenticated users can comment on posts.
- List Comments – checks comments list with pagination for a given post.
- Update Own Comment – ensures only the comment author can update their content.
- Delete Other’s Comment Forbidden – validates that users cannot delete comments they don’t own.

Sample Output (truncated):

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 1.678s

OK


------------------------------------------

Notification Tests:

1. Like a post

- Endpoint: POST /posts/{id}/like/
- Expected: 
    * Response: { "status": "liked" }
    * Post’s likes count increases
    * A new Notification is created for the post owner

2. Unlike a post
- Endpoint: POST /posts/{id}/unlike/
- Expected:
    * Response: { "status": "unliked" }
    * Post’s likes count decreases
    * No new notification should be created here

3. View notifications
- Endpoint: GET /notifications/
- Expected:
    * Returns a list of notifications
    * Check that the post owner sees a new notification when their post is liked
    * Mark a notification as read

4. Mark as read
- Endpoint: POST /notifications/{id}/mark_as_read/
- Expected:
    * That notification’s is_read becomes true


5. Mark all as read
- Endpoint: POST /notifications/mark_all_as_read/
- Expected:
    * All unread notifications for the user get marked as read

