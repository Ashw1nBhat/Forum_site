from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='student_home'),
    path('about/',views.about,name='student_about'),
]