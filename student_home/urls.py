from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,UserPostListView
from .import views

urlpatterns = [
    path('', PostListView.as_view() ,name='student_home'),
    path('user/<str:username>/', UserPostListView.as_view() ,name='student-questions'),
    path('question/<int:pk>/', PostDetailView.as_view() ,name='question-detail'),
    path('question/new/', PostCreateView.as_view() ,name='question-create'),
    path('about/',views.about,name='student_about'),
    path('announcements/',views.announcements,name='student_announce'),
]