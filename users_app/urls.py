from django.urls import path
from .views import login_view, register_view, profile_view

app_name = "users"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
]