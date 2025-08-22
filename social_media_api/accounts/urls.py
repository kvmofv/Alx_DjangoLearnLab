from django.urls import path
from .views import RegistrationView, LoginView, TokenView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name= 'register'),
    path("login/", LoginView.as_view(), name= 'login'),
    path("token/", TokenView.as_view(), name= 'token'),
]