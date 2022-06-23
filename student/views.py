from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .models import StudentResume,SkillList,ProjectList
from company.models import Job,Applicants,InvitedStudent,CompanyProfile, Selected
from quiz.models import Result
from manager.models import Notice,changesNote
from .forms import ResumeForm,SkillForm,ProjectForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
import datetime
# Create your views here.
#------------------------company Profile for students-------------------
def CompanyProfileStudent(request,key):
    cp=CompanyProfile.objects.get(id=key)
    jobs=Job.objects.filter(user=cp.user)
    context={
        'cp':cp,
        'jobs':jobs,
    }
    return render(request,'student/company_profile.html',context)
#--------------------------applied jobs list at home--------------------
def AppliedStudentList(request):
    applied=Applicants.objects.filter(applicant=request.user)
    context={
        'applied':applied,
    }
    return render(request,'student/applied_list.html',context)

#--------------------------invited for interview - for home-----------------------------
def InvitedStudentList(request):
    invited=InvitedStudent.objects.filter(invited_applicants=request.user)
    context={
        'invited':invited,
    }
    return render(request,'student/invited_list.html',context)
#-----------------------------test list for home-------------------------------
def TestStudents(request):
    applied=Applicants.objects.filter(applicant=request.user)


    context={
        'applied':applied
    }
    return render(request,'student/test_list.html',context)
#----------------------show student resume-------------------
def ShowStudentResume(request,key):
    User=get_user_model().objects.get(id=request.user.id)
    sr=StudentResume.objects.get(user=User)
    project_list=ProjectList.objects.filter(user=User)
    skill_list=SkillList.objects.filter(user=User)
    cgpa=int(sr.sem1)+int(sr.sem2)+int(sr.sem3)+int(sr.sem4)+int(sr.sem5)+int(sr.sem6)+int(sr.sem7)+int(sr.sem8)
    cgpa=cgpa/8
    date=datetime.date.today().strftime("%d/%m/%y")
    context={
        'User':User,
        'sr':sr,
        'project_list':project_list,
        'skill_list':skill_list,
        'cgpa':cgpa,
        'date':date,
    }
    return render(request,'student/resume.html',context)
#-------------------jobs view---------------------------
def Job_list(request):
    jobs=Job.objects.all().order_by('-date_posted')
    try:
        applied=Applicants.objects.filter(applicant=request.user)
    except Applicants.DoesNotExist:
        applied=False

    context={
        'jobs':jobs,
        'applied':applied,
    }
    return render(request,'student/job_list.html',context)

def JobDetailView(request,pk):
    jobs=Job.objects.get(id=pk)
    try:
        applied=Applicants.objects.get(job=jobs,applicant=request.user)
    except Applicants.DoesNotExist:
        applied=False

    try:
        sel=Selected.objects.get(selected_applicants=request.user)
    except Selected.DoesNotExist:
        sel=False
    print(sel)
    context={
        'jobs':jobs,
        'applied':applied,
        'sel':sel, 
    }
    return render(request,'student/job_detail.html',context)

def ApplyForJob(request,pk,key):
    jobs=Job.objects.get(id=pk)
    applicant_student=get_user_model().objects.get(id=key)

    a=Applicants(job=jobs,applicant=applicant_student)
    a.save()
    return redirect('job-detail-view',pk)

#--------------------------profile --------------------------------
def Profile_view(request,key):
    User=get_user_model().objects.get(id=key)
    sd=StudentResume.objects.get(user=User)
    project_list=ProjectList.objects.filter(user=User)
    skill_list=SkillList.objects.filter(user=User)
    cgpa=int(sd.sem1)+int(sd.sem2)+int(sd.sem3)+int(sd.sem4)+int(sd.sem5)+int(sd.sem6)+int(sd.sem7)+int(sd.sem8)
    cgpa=cgpa/8
    context={
        'User':User,
        'project_list':project_list,
        'skill_list':skill_list,
        'cgpa':cgpa,
    }
    return render(request,'student/student_profile.html',context)
#-----------------main page -------------------------

def home_view(request,key):
    User=get_user_model().objects.get(id=key)
    
    notice=Notice.objects.all().order_by('-date_posted')
    
    ap_count=Applicants.objects.filter(applicant=User).count()
    inv_count=InvitedStudent.objects.filter(invited_applicants=User).count()
    try:
        sd=StudentResume.objects.get(user=User)
        cn=changesNote.objects.filter(student=sd)
    except StudentResume.DoesNotExist:
        cn=False

    try:
        sel=Selected.objects.get(selected_applicants=request.user)
    except Selected.DoesNotExist:
        sel=False    

    context={
        'User':User,
        'notice':notice,
        'cn':cn,
        'ap_count':ap_count,
        'inv_count':inv_count,
        'sel':sel,
    }
    return render(request,'student/student_home.html',context)
    
def CloseButton(request,key):
    key1=request.user.id
    print("hello")
    cn=changesNote.objects.get(id=key)
    cn.is_notified=True
    cn.save()


    return redirect('shome',key1)

#-----------project view-----------------------
class AddProjectView(CreateView):
    model=ProjectList
    form_class=ProjectForm
    template_name='student/add_project.html'

    def get_context_data(self,*args,**kwargs):
        project_list=ProjectList.objects.filter(user=self.request.user)
        context=super(AddProjectView,self).get_context_data(*args,**kwargs)

        context['project_list']=project_list
        return context

class UpdateProjectView(UpdateView):
    model=ProjectList
    form_class=ProjectForm
    template_name='student/edit_project.html'

class DeleteProjectView(DeleteView):
    model=ProjectList
    success_url=reverse_lazy("add-project")
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

#-----------skill view-------------------------


class AddSkillView(CreateView):
    model=SkillList
    form_class=SkillForm
    template_name='student/add_skill.html'

    def get_context_data(self,*args,**kwargs):
        Skill_list=SkillList.objects.filter(user=self.request.user)
        context=super(AddSkillView,self).get_context_data(*args,**kwargs)

        context['skill_list']=Skill_list
        return context

class UpdateSkillView(UpdateView):
    model=SkillList
    form_class=SkillForm
    template_name='student/edit_skill.html'

    

class DeleteSkillView(DeleteView):
    model=SkillList
    success_url=reverse_lazy("add-skills")
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

#----------------Resume view------------------------------
class CreateResumeView(CreateView):
    model=StudentResume
    form_class=ResumeForm
    template_name='student/student_resume.html'

class EditResumeView(UpdateView):
    model=StudentResume
    form_class=ResumeForm
    template_name='student/edit_resume.html'

    def post(self, request, **kwargs):
        self.object = self.get_object()
        print(self.object)
        self.object.is_verified=False
        self.object.save()
        return super(EditResumeView, self).post(request, **kwargs)

