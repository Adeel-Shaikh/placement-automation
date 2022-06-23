from django.db import models
from django.contrib.auth import get_user_model
from company.models import Job
# Create your models here.
class Quiz(models.Model):
    quiz_for=models.OneToOneField(Job,on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=300)
    num_questions = models.IntegerField(default=0)

    

    def __str__(self):
        return self.quiz_title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
    question_num = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question)+" || "+str(self.choice_text)

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)
