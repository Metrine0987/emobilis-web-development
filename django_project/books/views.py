from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def blog_details(request):
    return render(request, "blog-details.html")

def custom_404(request):
    return render(request, "404.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")

def service_details(request):
    return render(request, "service-details.html")

def starter_page(request):
    return render(request, "starter-page.html")