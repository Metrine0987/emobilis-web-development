from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, "add_student.html")