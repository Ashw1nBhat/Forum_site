from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone






class Question(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE) 
    subject = models.CharField(max_length=15)
    question_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ("can_update", "Can update questions"),
        ]
    

    
    def __str__(self):
        return str(self.question_text)

    

        

 
class Answer(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE) 
    answer_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    a_question = models.OneToOneField(Question, on_delete=models.CASCADE )

    class Meta:
        permissions = [
            ("can_answer", "Can answer questions"),
        ]
    
    
    def __str__(self):
        return str(self.poster) 

          

