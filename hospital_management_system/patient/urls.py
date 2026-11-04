from patient import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("book_appointment/", views.book_appointment, name="book_appointment"),
]