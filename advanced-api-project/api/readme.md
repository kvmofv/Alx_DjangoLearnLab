Testing Instructions:

Testing Strategy:

We use Django REST Framework’s built-in testing tools (APITestCase) to verify all CRUD operations, authentication requirements, and permission enforcement for the Book model.

What you Test:

Create Book: Validates POST endpoint and required fields.
Retrieve Book: Tests access to a single book’s data.
List Books: Confirms all books are returned to authenticated users.
Update Book: Ensures PUT/PATCH methods update data correctly.
Delete Book: Verifies books are removed properly.
Permissions: Ensures unauthorized users are denied access to protected endpoints.

how to run:

python manage.py test api

Test Results:

OK: All tests passed.
FAIL: One or more tests failed (details will be shown in the terminal).
To re-run, fix the errors in views/tests and rerun the command.
