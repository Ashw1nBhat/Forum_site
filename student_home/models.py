from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse




class Question(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE) 
    subject = models.CharField(max_length=15)
    question_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.subject

        

    

