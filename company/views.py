from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,UpdateView
from .models import CompanyProfile,Job,Applicants,Selected,Rejected,InvitedStudent
from student.models import StudentResume,ProjectList,SkillList
from quiz.models import Result,Quiz
from .forms import CreateCompanyForm,JobForm
from django.shortcuts import redirect
import datetime
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home_view(request,key):
    User=get_user_model().objects.get(id=key)
    jobs=Job.objects.filter(user=request.user)
    applicant_count=Applicants.objects.filter(job__id__in=jobs.all()).count()
    invited_count=InvitedStudent.objects.filter(job__id__in=jobs.all()).count()
    selected_count=Selected.objects.filter(job__id__in=jobs.all()).count()
    context={
        'User':User,
        'applicant_count':applicant_count,
        'invited_count':invited_count,
        'selected_count':selected_count,
    }
    return render(request,'company/company_home.html',context)
#--------------------company Profile------------------------------------
def CompanyProfilePage(request):
    cp=CompanyProfile.objects.get(user=request.user)
    jobs=Job.objects.filter(user=request.user)
    context={
        'cp':cp,
        'jobs':jobs
    }
    return render(request,'company/company_profile.html',context)
#----------------------applicant list for home-----------------------
def ApplicantHomeView(request):
    jobs=Job.objects.filter(user=request.user)
    applicant=Applicants.objects.filter(job__id__in=jobs.all())
    context={
        'jobs':jobs,
        'applicant':applicant,
    }
    return render(request,'company/applicant_home.html',context)
#-----------------------invited list for home---------------------------
def InvitedHomeView(request):
    jobs=Job.objects.filter(user=request.user)
    invited=InvitedStudent.objects.filter(job__id__in=jobs.all())
    
    context={
        'jobs':jobs,
        'invited':invited,
    }
    return render(request,'company/invited_home.html',context)

#---------------------selected list for home------------------------
def SelectedHomeView(request):
    jobs=Job.objects.filter(user=request.user)
    selected=Selected.objects.filter(job__id__in=jobs.all())
    context={
        'jobs':jobs,
        'selected':selected,
    }
    return render(request,'company/selected_home.html',context)

#------------------test stats----------------------------
def TestStats(request,key):
    q=Quiz.objects.get(id=key)
    res=Result.objects.filter(quiz=q)
    context={
        'q':q,
        'res':res,
    }
    return render(request,'company/test_stats.html',context)
#----------------job hididng------------------------
def HideJob(request,key):
    job=Job.objects.get(id=key)
    if job.hide_key==True:
        job.hide_key=False
    else:
        job.hide_key=True
    job.save()
    return redirect('jobs-list')
#-----------------jobs------------------------------
class CreateJobview(CreateView):
    model=Job
    form_class=JobForm
    template_name='company/add_job.html'

def JobList(request):
    job_list=Job.objects.filter(user=request.user)
    #job_count=Job.objects.filter(user=request.user).count()

    context={
        'job_list':job_list,
    }
    return render(request,'company/job_list.html',context)

def ApplicantList(request,key):
    applicant_list=Applicants.objects.filter(job=key)

    context={
        'applicant_list':applicant_list,
    }
    return render(request,'company/applicant_list.html',context)
#--------------------selected boisss-----------------------------------
def SelectedStudent(request,key1,key):
    jobs=Job.objects.get(id=key1)
    selected_student=get_user_model().objects.get(id=key)
    key2=selected_student.studentresume.id

    a=Selected(job=jobs,selected_applicants=selected_student)
    a.save()
    b=InvitedStudent.objects.get(job=jobs,invited_applicants=selected_student).delete()
    c=Applicants.objects.filter(applicant=selected_student).delete()
    
    subject = f'SLECTED for {jobs.position} '
    message = f'Hi {selected_student.first_name} {selected_student.last_name}, selected!\n stay tune for further details\n\n\n By {jobs.user.companyprofile} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [selected_student, ]
    send_mail( subject, message, email_from, recipient_list )

    return redirect('student-resume-c',key1,key2)
    
#---------------------------invited yesss----------------------
def Invitedstudents(request,key1,key):
    jobs=Job.objects.get(id=key1)
    invited_student=get_user_model().objects.get(id=key)
    key2=invited_student.studentresume.id

    a=InvitedStudent(job=jobs,invited_applicants=invited_student)
    a.save()

    subject = f'Invited for Interview of {jobs.position} '
    message = f'Hi {invited_student.first_name} {invited_student.last_name}\n stay tune for further details.\n\n\n By {jobs.user.companyprofile} '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [invited_student, ]
    send_mail( subject, message, email_from, recipient_list )

     
    return redirect('student-resume-c',key1,key2)
#--------------------------rejected oops------------------------
def RejectedStudent(request,key1,key):
    jobs=Job.objects.get(id=key1)
    rejected_student=get_user_model().objects.get(id=key)
    key2=rejected_student.studentresume.id

    a=Rejected(job=jobs,rejected_applicants=rejected_student)
    a.save()
    return redirect('student-resume-c',key1,key2)

def RevertRejected(request,key):
    revert=Rejected.objects.get(id=key)
    key1=revert.job.id
    key2=revert.rejected_applicants.studentresume.id
    revert.delete()
    return redirect('student-resume-c',key1,key2)

#------------------student resume---------------------------------
def StudentResumeView(request,key1,key):
    jb=Job.objects.get(id=key1)
    sr=StudentResume.objects.get(id=key)
    User=get_user_model().objects.get(email=sr)
    project_list=ProjectList.objects.filter(user=User)
    skill_list=SkillList.objects.filter(user=User)
    cgpa=int(sr.sem1)+int(sr.sem2)+int(sr.sem3)+int(sr.sem4)+int(sr.sem5)+int(sr.sem6)+int(sr.sem7)+int(sr.sem8)
    cgpa=cgpa/8
    date=datetime.date.today().strftime("%d/%m/%y")

    try:
        res=Result.objects.get(user=User)
    except Result.DoesNotExist:
        res=False


    try:
        select=Selected.objects.get(job=jb,selected_applicants=User)
    except Selected.DoesNotExist:
        select=False

    try:
        reject=Rejected.objects.get(job=jb,rejected_applicants=User)
    except Rejected.DoesNotExist:
        reject=False
    
    try:
        invite=InvitedStudent.objects.get(job=jb,invited_applicants=User)
    except InvitedStudent.DoesNotExist:
        invite=False
    context={
        'sr':sr,
        'User':User,
        'jb':jb,
        'select':select,
        'reject':reject,
        'project_list':project_list,
        'skill_list':skill_list,
        'cgpa':cgpa,
        'date':date,
        'invite':invite,
        'res':res,
    }
    return render(request,'company/student_resume.html',context)

#--------------------company profile--------------------------
class CreateCompanyProfile(CreateView):
    model=CompanyProfile
    form_class=CreateCompanyForm
    template_name='company/add_profile.html'

class EditCompanyProfile(UpdateView):
    model=CompanyProfile
    form_class=CreateCompanyForm
    template_name='company/edit_profile.html'