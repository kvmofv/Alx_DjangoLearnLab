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
