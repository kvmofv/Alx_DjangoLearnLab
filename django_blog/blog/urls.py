from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, ProfileView, ProfileUpdateView, home_view, CreatePostView, ListPostView, UpdatePostView, DeletePostView, DetailPostView

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('posts/', ListPostView.as_view(), name='posts'),
    path('post/new/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='view_post' ),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
]