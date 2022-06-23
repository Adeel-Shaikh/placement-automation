from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
skill_level_list=(
    ('Basic','Basic'),
    ('InterMediate','Intermediate'),
    ('Advance','Advance')
)
class SkillList(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=125)
    skill_type=models.CharField(max_length=50)
    skill_level=models.CharField(max_length=25,choices=skill_level_list)

    def __str__(self):
        return str(self.user)+" | "+self.skill_name

    def get_absolute_url(self):
        return reverse("add-skills")

semester_choice=(
    ('3','III'),
    ('4','IV'),
    ('5','V'),
    ('6','VI'),
    ('7','VII'),
    ('8','VII'),
)
class ProjectList(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    project_title=models.CharField(max_length=200)
    project_description=models.TextField()
    semester=models.CharField(max_length=3, choices=semester_choice,default='3')
    def __str__(self):
        return str(self.user)+" | "+self.project_title

    def get_absolute_url(self):
        return reverse("add-project")

gender_choice_list=(
    ('M','Male'),
    ('F','Female'),
    ('Other','Prefer Not to Say')
)
branch_names=(
    ('Computer Engineering','Computer Engineering'),
    ('Information Technology','Information Technology'),
    ('Automobile Engineering','Automobile Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),
    ('Chemical Engineering','Chemical Engineering'),
    ('Electronics And Telecommunication','Electronics And Telecommunication'),
    ('Electronics Engineering','Electronics Engineering')

)

class StudentResume(models.Model):
    user=models.OneToOneField(get_user_model(),null=True,on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=10)
    email2=models.EmailField()
    address=models.TextField()
    addmission_no=models.CharField(max_length=11,default=00000000)
    dob=models.DateField()
    gender=models.CharField(max_length=20,choices=gender_choice_list)
    branch=models.CharField(max_length=300,choices=branch_names)
    college=models.CharField(max_length=200,default="Pillai College Of Engineering")
    ssc=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    ssc_college=models.CharField(max_length=200)
    hsc=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    hsc_college=models.CharField(max_length=200,default="null")
    diploma=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    diploma_college=models.CharField(max_length=200,default="null")
    sem1=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem2=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem3=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem4=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem5=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem6=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem7=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    sem8=models.DecimalField(max_digits=5,decimal_places=2,default=0.00,null=True)
    attendance=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    Backlogs=models.IntegerField(default=0.0)
    #skills=models.ManyToOneField(get_user_model(),null=True,on_delete=models.CASCADE)
    career_obj=models.TextField()
    linkden_url=models.CharField(max_length=100,null=True)
    github_url=models.CharField(max_length=100,null=True)
    is_verified=models.BooleanField(default=False)
    is_notified=models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('shome',kwargs={'key':self.user.id})