from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def home(request):
    questions = {
        'posts': Question.objects.all()
    }
    return render(request, 'student_home/student-home.html',questions)

def about(request):
    return render(request, 'student_home/student-about.html',{'subject':'About'})