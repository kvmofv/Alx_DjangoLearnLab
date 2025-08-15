Authentication System Documentation

Overview:
- This authentication system is built using Django’s built-in authentication framework, extended with custom views, forms, and templates to provide user registration, login, logout, and profile management features.

Users can:
- Create a new account.
- Log in and log out securely.
- View their profile details.
- Edit their username, email, profile picture, and bio.

------------------
1. Models
- User (Django’s built-in model)
    = Handles username, password, email, and core authentication fields.

- Profile (Custom model in blog/models.py)
    = Extends the user with: image (profile picture), bio (short biography), Linked to User via OneToOneField.

2. Forms
- RegistrationForm: 
    = Extends UserCreationForm to include email.
- UserUpdateForm:
    = Updates username and email.
- ProfileUpdateForm:
    = Updates image and bio.

3. Views
Registration View (RegistrationView)
Class-based view (CreateView):       Displays registration form, validates data, and creates new user accounts.
Login View (LoginView):              Django’s built-in CBV for logging users in.
Logout View (LogoutView):            Django’s built-in CBV for logging users out.
Profile View (ProfileView):          Displays the authenticated user’s profile details.
Profile Edit View (ProfileEditView): Displays and processes forms for updating both User and Profile data.

4. Templates:

Located in templates/:
1. registration/login.html:    User login form.
2. registration/register.html: New user registration form.
3. registration/logout.html:   Logout confirmation.
4. profile.html:               Displays the user’s profile information.
5. profile_edit.html:          Combined form to edit both User and Profile.

**Templates extend base.html and use the provided CSS/JS for styling.

5. URLs
- Project-level (project/urls.py):

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


- App-level (blog/urls.py):

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]

--------------|
How It Works: |
--------------|

1. Registration:
- User fills out the registration form.
- On successful submission, a User object is created, and a linked Profile is automatically created via signals.

2. Login
- User enters their credentials on login.html.
- Django’s authentication backend validates credentials.
- On success, user is redirected to their profile or home page.

3. Logout
- Logs the user out and displays a logout confirmation page.

4. Profile Viewing
- Only available to logged-in users (LoginRequiredMixin).
- Displays username, email, bio, and profile picture.

5. Profile Editing
- Two forms (UserUpdateForm + ProfileUpdateForm) are shown together.
- On submit, updates both User and Profile data.
- Uploaded images are stored in MEDIA_ROOT/profile_pics/.

--------------------|
Testing Instructions|
--------------------|

1. Registration

- Navigate to /register/.
- Fill in username, email, and password.
- Check:
    = User appears in Django Admin (/admin/).
    = A linked Profile is automatically created.

2. Login

- Navigate to /login/.
- Enter correct credentials
    = Redirect to the profile page.
- Enter wrong credentials
    = Display error messages.

3. Logout
- Navigate to /logout/.
    = Display confirmation and log out the user.

4. Profile View
- Log in and go to /profile/.
- Confirm correct details are displayed.

5. Profile Edit
- Navigate to /profile/edit/.
- Update username, email, bio, and image.
- Submit and verify changes appear on the profile page.

------------------------------------------
for task 2:

1. Templates Created
- delete_post.html – Confirmation page for deleting a post, extends blog/base.html and loads static files.
- update_post.html – Post update form page, extends blog/base.html and loads static files.
- detail_post.html – Displays the full content of a single post, extends blog/base.html and loads static files.

2. Form Integration
- Added form rendering in update_post.html (and create_post.html) using {{ form.as_p }} for displaying form fields.

3. Permissions & Access Control
- Updated UpdateView and DeleteView to include:
-LoginRequiredMixin – Only authenticated users can access update/delete.
-UserPassesTestMixin – Only the post’s author can update/delete their own posts.
- Implemented test_func() to check if the logged-in user is the author.

4. Post Creation Permission
- Ensured CreateView requires login via LoginRequiredMixin.

----------------------------------------

Tagging & Search Features

Adding Tags to Posts
- When creating or editing a post, locate the Tags input field in the form.
- Enter one or more tags separated by commas (e.g., django, python, backend).
- Tags should be short and descriptive.
- Tags are case-insensitive (Python and python are treated the same).
- Click Save to apply the tags to the post.

Browsing by Tags
- On the blog’s post list or individual post pages, tags are displayed under the post title or content.
- Click on a tag to view all posts associated with it.

Using the Search Bar
- The search bar is available at the top of the post listing page.
- Enter keywords to search in post titles, content, or tags.
- Search results are filtered automatically based on your input.

Examples:
- Searching for django shows all posts tagged with "django" or containing "django" in the content/title.
- Clicking the tag python shows only posts related to Python.
