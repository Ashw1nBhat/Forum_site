from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'poster':'ashwin',
        'subject':'DAA',
        'question':'first post content',
        'date_posted':'Mar 8 2018'
    },
     {
        'poster':'abhishek',
        'subject':'DAA',
        'question':'first post content',
        'date_posted':'Mar 8 2018'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'student_home/student-home.html',context)

def about(request):
    return render(request, 'student_home/student-about.html',{'subject':'About'})