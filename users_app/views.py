from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    if request.method == "POST":
        print(request.POST)
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:main-page'))
    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, "users/login.html", context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
    form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)