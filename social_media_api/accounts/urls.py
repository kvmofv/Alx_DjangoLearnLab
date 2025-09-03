from django.urls import path
from .views import RegistrationView, LoginView, TokenView, FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name= 'register'),
    path("login/", LoginView.as_view(), name= 'login'),
    path("token/", TokenView.as_view(), name= 'token'),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]