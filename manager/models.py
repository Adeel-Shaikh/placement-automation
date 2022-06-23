from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.expressions import F
from django.utils import timezone
from django.urls import reverse
from student.models import StudentResume

# Create your models here.
class Notice(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    college_name=models.CharField(max_length=220,default="Pillai College Of Engineering")
    topic=models.CharField(max_length=220)
    description=models.TextField()
    event_date=models.DateField()
    organized_by=models.CharField(max_length=200)
    students_eligible=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    hide_key=models.BooleanField(default=False)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('notice-home')

class changesNote(models.Model):
    student=models.ForeignKey(StudentResume,on_delete=models.CASCADE)
    note=models.TextField()
    is_notified=models.BooleanField(default=False)

    def __str__(self):
        return "changes to "+str(self.student)