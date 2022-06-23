from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Notice, changesNote
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from company.models import Applicants,Selected,Job,CompanyProfile
from student.models import StudentResume,ProjectList,SkillList
from .forms import NoticeForm,ChangesForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Count
import datetime


# Create your views here.
def home_view(request,key):
    User=get_user_model().objects.get(id=key)
    jb=Job.objects.all()
    jbs=[]
    apps=[]
    selects=[]
    for j in jb:
        name=j.position +" By "+j.user.companyprofile.company_name
        jbs.append(name)
        app=Applicants.objects.filter(job=j).count()
        apps.append(app)
        s=Selected.objects.filter(job=j).count()
        selects.append(s)

    context={
        'User':User,
        'apps':apps,
        'jbs':jbs,
        'selects':selects
    }
    return render(request,'manager/manager_home.html',context)
#---------------------selected students-------------------------
def SelectedStudentList(request):
    jb=Job.objects.all()
    sl=Selected.objects.all()
    context={
        'jb':jb,
        'sl':sl,
    }
    return render(request,'manager/selected_student.html',context)

#------------------applied students-------------------------
def AppliedStudentList(request):
    jb=Job.objects.all()
    al=Applicants.objects.all()
    sl=Selected.objects.all()
    context={
        'jb':jb,
        'al':al,
        'sl':sl,
    }
    return render(request,'manager/applicant_student.html',context)
#----------------------------jobs list-----------------------
def JobListManager(request):
    cp=get_user_model().objects.filter(user_type='company')

    jb=Job.objects.filter(user__id__in=cp.all())

    context={
        'cp':cp,    
        'jb':jb,
    }
    return render(request,'manager/jobs_list.html',context)
    
#--------------------verify students----------------------
def FinalVerify(request,key):
    sr=StudentResume.objects.get(id=key)
    sr.is_verified=True
    sr.save()

    return redirect('verify-resume',key)

def VerifyStudent(request):

    st=StudentResume.objects.all().order_by('branch')
    print(st)
    context={
        'st':st,
    }
    return render(request,'manager/verify_list.html',context)

def VerifyResume(request,key):
    sr=StudentResume.objects.get(id=key)
    User=get_user_model().objects.get(email=sr)
    project_list=ProjectList.objects.filter(user=User)
    skill_list=SkillList.objects.filter(user=User)
    date=datetime.date.today().strftime("%d/%m/%y")
    cgpa=int(sr.sem1)+int(sr.sem2)+int(sr.sem3)+int(sr.sem4)+int(sr.sem5)+int(sr.sem6)+int(sr.sem7)+int(sr.sem8)
    cgpa=cgpa/8
    chng=changesNote.objects.filter(student=sr)
    if request.method== 'POST':
        form=ChangesForm(request.POST)
        note=request.POST['note']
        cn=changesNote(student=sr,note=note)
        form=ChangesForm()
        cn.save()
        if sr.is_verified==True:
            sr.is_verified=False
            sr.save()

        return redirect('verify-resume',key)
    else:
        form=ChangesForm()

    context={
        'sr':sr,
        'User':User,
        'project_list':project_list,
        'skill_list':skill_list,
        'date':date,
        'cgpa':cgpa,
        'form':form,
        'chng':chng,
    }
    return render(request,'manager/verify_resume.html',context)
#------------------------------notice----------------------------
def HideNotice(request,key):
    key=Notice.objects.get(id=key)
    print(key.hide_key)
    if key.hide_key == False:
        key.hide_key=True
    else:
        key.hide_key=False
    key.save()

    return redirect('notice-home')


class AddNoticeView(CreateView):
    model=Notice
    form_class=NoticeForm
    template_name='manager/add_notice.html'

class NoticeHomeView(ListView):
    model=Notice
    template_name='manager/notice_home.html'
    ordering= ['-date_posted']

class NoticeEditView(UpdateView):
    model=Notice
    form_class=NoticeForm
    template_name='manager/notice_edit.html'

class DeleteNoticeView(DeleteView):
    model=Notice
    success_url=reverse_lazy('notice-home')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)