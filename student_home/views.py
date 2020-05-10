from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Question,Answer
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




class PostUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Question
    permission_required = 'student_home.can_update'
    fields = ['subject','question_text']
    success_url = reverse_lazy('student_home')  

   

      


class PostDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Question
    permission_required = 'student_home.can_update'
    success_url = '/'  

     


def about(request):
    return render(request, 'student_home/student-about.html', {'title': 'About'})

def announcements(request):
    return render(request, 'student_home/student-announce.html', {'title': 'Announcements'})                              
    



class AnswerCreateView(PermissionRequiredMixin,CreateView):
    model = Answer
    permission_required = 'student_home.can_answer'
    fields = ['a_question','answer_text']
    success_url = reverse_lazy("student_home")  

    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin ,PermissionRequiredMixin,UpdateView):
    model = Answer
    permission_required = 'student_home.can_answer'
    fields = ['a_question','answer_text']
    success_url = '/' 

   
    def form_valid(self,form):
        form.instance.poster = self.request.user 
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False  


class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin ,PermissionRequiredMixin,DeleteView):
    model = Answer
    permission_required = 'can_answer'
    success_url = '/'  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False          

       

 


