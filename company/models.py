from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Job(models.Model):
    user=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)
    position=models.CharField(max_length=200)
    expected=models.TextField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    vacancy=models.IntegerField()
    desc=models.TextField()
    job_time=models.DecimalField(max_digits=4,decimal_places=2)
    job_responsibilty=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    hide_key=models.BooleanField(default=False)

    
    def __str__(self):
        return self.position+" | "+str(self.user)

    def get_absolute_url(self):
        return reverse("jobs-list")

class Applicants(models.Model):
    job=models.ForeignKey(Job,null=True,on_delete=models.CASCADE)
    applicant=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)
    date_of_application=models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.applicant)+" | "+str(self.job)
        
class InvitedStudent(models.Model):
    job=models.ForeignKey(Job,null=True,on_delete=models.CASCADE)
    invited_applicants=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invited_applicants)


class Selected(models.Model):
    job=models.ForeignKey(Job,null=True,on_delete=models.CASCADE)
    selected_applicants=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)
    date_of_application=models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.selected_applicants)

class Rejected(models.Model):
    job=models.ForeignKey(Job,null=True,on_delete=models.CASCADE)
    rejected_applicants=models.ForeignKey(get_user_model(),null=True,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.rejected_applicants)
        
type_list=(
    ('public','Publicly held'),
    ('private','Privately held')
)
class CompanyProfile(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    company_name=models.CharField(max_length=70)
    preview=models.TextField()
    about=models.TextField()
    website=models.URLField(max_length=250)
    service_provided=models.CharField(max_length=250)
    address=models.TextField()
    headquaters=models.CharField(max_length=250)
    type_of_company=models.CharField(choices=type_list,max_length=50)
    founded_on=models.CharField(max_length=4)
    speciality=models.TextField()

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("company-profile")