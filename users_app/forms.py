from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import Users


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Foydalanuvchi nomini kiriting!"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Parolni kiriting!"
    }))
    class Meta:
        model = Users
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Ismingizni kiriting!"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Familiyangizni kiriting!"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Foydalanuvchi nomini kiriting!"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Emailingizni kiriting!"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Parol kiriting!"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placceholder": "Parolni takrorlang!"}))
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

class ProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "custom-file-input"}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4", "readonly": True}))
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "username", "email", "image")

