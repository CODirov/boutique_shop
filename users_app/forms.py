import uuid
from datetime import timedelta

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.utils.timezone import now

from .models import Users, EmailVerification


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
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        expiration = now()+timedelta(hours=48)
        record = EmailVerification.objects.create(user=user, expiration=expiration, code=uuid.uuid4())
        record.send_verification_email()
        return user

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

