from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, ProfileView, ProfileUpdateView, home_view, CreatePostView, PostListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('', home_view, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
]