from django.urls import path
from .views import PostListView,PostCreateView,UserPostListView,PostDetailView,AnswerCreateView,PostUpdateView,PostDeleteView
from .import views


urlpatterns = [
    path('', PostListView.as_view() ,name='student_home'),
    path('user/<str:username>/', UserPostListView.as_view() ,name='student-questions'),
    path('question/<int:id>/', PostDetailView,name='question-detail'),
    path('question/<int:pk>/update/', PostUpdateView.as_view(),name='question-update'),
    path('question/<int:pk>/delete/', PostDeleteView.as_view(),name='question-delete'),
    path('answer/',AnswerCreateView.as_view(),name = 'answer-create'),
    path('question/new/', PostCreateView.as_view() ,name='question-create'),
    path('about/',views.about,name='student_about'),
    path('announcements/',views.announcements,name='student_announce'),
]