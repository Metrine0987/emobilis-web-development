from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def profile(request):
    return render(request, "profile.html")

def book_appointment(request):
    return render(request, "book_appointment.html")