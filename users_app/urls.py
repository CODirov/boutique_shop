from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (UserLoginView, UserRegisterView, UserProfileView)

app_name = "users"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]