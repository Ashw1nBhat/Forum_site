from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView
from .models import Question
from django.urls import reverse_lazy


def home(request):
    context = {
        'posts': Question.objects.all()
    }
    return render(request, 'student_home/student-home.html',context)


class PostListView(ListView):
    model = Question
    template_name = 'student_home/student-home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Question
    template_name = 'student_home/student_questions.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(poster=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Question  

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['subject','question_text']
    success_url = reverse_lazy('student_home')  

    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)
    

def about(request):
    return render(request, 'student_home/student-about.html', {'title': 'About'})

def announcements(request):
    return render(request, 'student_home/student-announce.html', {'title': 'Announcements'})    