from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('posts/', views.ListPostView.as_view(), name='posts'),
    path('post/new/', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='post_detail' ),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),
    path('post/<int:post_id>/comments/', views.ListCommentView.as_view(), name='comment_list'),
    path('post/<int:post_id>/comments/new/', views.CreateCommentView.as_view(), name='create_comment'),
    path('post/<int:post_id>/comments/<int:pk>/update/', views.UpdateCommentView.as_view(), name='update_comment'),
    path('post/<int:post_id>/comments/<int:pk>/delete', views.DeleteCommentView.as_view(), name='delete_comment'),
]