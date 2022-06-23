from django.urls import path
from .views import home_view,CreateResumeView,EditResumeView,AddSkillView,UpdateSkillView,DeleteSkillView,AddProjectView,UpdateProjectView,DeleteProjectView,Profile_view,Job_list,JobDetailView,ApplyForJob,ShowStudentResume,AppliedStudentList,InvitedStudentList,CompanyProfileStudent,TestStudents,CloseButton


urlpatterns=[
    path('<int:key>/',home_view,name='shome'),
    path('resume/',CreateResumeView.as_view(),name='student-resume'),
    path('resume/edit/<int:pk>',EditResumeView.as_view(),name='edit-resume'),
    path('skill/',AddSkillView.as_view(),name="add-skills"),
    path('skill/edit/<int:pk>',UpdateSkillView.as_view(),name="edit-skills"),
    path('skill/delete/<int:pk>',DeleteSkillView.as_view(),name="delete-skills"),
    path('project/',AddProjectView.as_view(),name="add-project"),
    path('project/edit/<int:pk>',UpdateProjectView.as_view(),name="edit-project"),
    path('project/delete/<int:pk>',DeleteProjectView.as_view(),name="delete-project"),
    path('profile/<int:key>/',Profile_view,name="student-profile"),
    path('jobs/',Job_list,name="job-list-view"),
    path('jobs/detail/<int:pk>/',JobDetailView,name="job-detail-view"),
    path('jobs/<int:pk>/<int:key>/',ApplyForJob,name="job-apply-view"),
    path('studentresume/<int:key>',ShowStudentResume,name="show-resume"),
    path('appliedjobs/',AppliedStudentList,name="applied-job-list"),
    path('invite/',InvitedStudentList,name="invited-jobs-list"),
    path('companyprofile/<int:key>',CompanyProfileStudent,name="company-profile-student"),
    path('test/',TestStudents,name='test-for-student'),
    path('close/<int:key>',CloseButton,name='close-notification'),




]
