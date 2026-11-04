from student import views
from django.urls import path

urlpatterns = [
    path("add_student/", views.add_student, name="add_student"),
]