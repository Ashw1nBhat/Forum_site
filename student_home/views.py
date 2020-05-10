from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Question,Answer
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator



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
    paginate_by = 3

class UserPostListView(ListView):
    model = Question
    template_name = 'student_home/student_questions.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(poster=user).order_by('-date_posted')


def PostDetailView(request,id):
    sc = Answer.objects.filter(a_question = id)

    if sc.count() > 0:
        context = {
        'questions':Question.objects.get(id= id),
        'answers':Answer.objects.get(a_question = id)
        }
    else:
        context = {
        'questions':Question.objects.get(id= id),
        
        }

        
    
    return render(request, 'student_home/question_detail.html',context)

    
  

    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['subject','question_text']
    success_url = reverse_lazy('student_home')  

   
    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,PermissionRequiredMixin,UpdateView):
    model = Question
    permission_required = 'can_update'
    fields = ['subject','question_text']
    success_url = reverse_lazy('student_home')  

   
    def form_valid(self,form):
        form.instance.poster = self.request.user 
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False  


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Question
    success_url = '/'  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False                    
    

class AnswerCreateView(CreateView):
    model = Answer
    fields = ['a_question','answer_text']
    success_url = reverse_lazy("student_home")  

    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

 


def about(request):
    return render(request, 'student_home/student-about.html', {'title': 'About'})

def announcements(request):
    return render(request, 'student_home/student-announce.html', {'title': 'Announcements'})    