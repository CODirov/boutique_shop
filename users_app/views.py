from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from products_app.models import Basket
from .models import Users, EmailVerification


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    success_message = "Siz muvaffaqiyatli tarzda ro'yxatdan o'tdingiz!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Ro'yxatdan o'tish"
        return context


class UserProfileView(SuccessMessageMixin, UpdateView):
    model = Users
    form_class = ProfileForm
    template_name = "users/profile.html"
    success_message = "Ma'lumotlar yangilandi!"
    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id, ))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context["title"] = "Shaxsiy kobinet"
        return context

class EmailVerificationView(TemplateView):
    template_name = "users/email_verification.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Email manzilni tasdiqlash!"
        return context

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Users.objects.get(email=kwargs["email"])
        print(user)
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("main-page"))