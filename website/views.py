from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# ================= HOME =================

def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def services(request):
    return render(request, "website/services.html")


def contact(request):
    return render(request, "website/contact.html")


# ================= LOGIN =================

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")   # customers dashboard

        messages.error(request, "Invalid Username or Password")

    return render(request, "website/login.html")


# ================= SIGNUP =================

def signup_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account Created Successfully")
        return redirect("login")

    return render(request, "website/signup.html")


# ================= LOGOUT =================

def logout_view(request):
    logout(request)
    return redirect("login")


# ================= DASHBOARD (Protected) =================

@login_required(login_url="login")
def dashboard(request):
    return redirect("customers:dashboard")   # customers app dashboard