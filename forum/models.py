from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField
from company.models import CompanyProfile

# Create your models here.


class Query(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = RichTextField()
    sub_forum = models.CharField(max_length=250)
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.title)+" by " + str(self.user)


class Reply(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question = models.ForeignKey(Query, on_delete=models.CASCADE)
    body = RichTextField()
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return "reply to "+str(self.question)
