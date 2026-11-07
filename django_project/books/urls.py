
from books import views
from django.urls import path


urlpatterns = [
    path("home/", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("blog-details/", views.blog_details, name="blog-details"),
    path("404/", views.custom_404, name="custom_404"),
    path("portfolio-details/", views.portfolio_details, name="portfolio-details"),
    path("service-details/", views.service_details, name="service-details"),
    path("starter-page/", views.starter_page, name="starter-page"),
]