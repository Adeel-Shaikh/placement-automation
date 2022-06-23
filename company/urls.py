from django.urls import path
from .views import home_view,CreateCompanyProfile,EditCompanyProfile,CreateJobview,JobList,ApplicantList,StudentResumeView,SelectedStudent,HideJob,RejectedStudent,RevertRejected,Invitedstudents,ApplicantHomeView,InvitedHomeView,SelectedHomeView,CompanyProfilePage,TestStats

urlpatterns=[
    path('<int:key>',home_view,name='chome'),
    path('create/',CreateCompanyProfile.as_view(),name="create-c-profile"),
    path('edit/<int:pk>',EditCompanyProfile.as_view(),name="edit-c-profile"),
    path('jobs/',CreateJobview.as_view(),name="create-jobs"),
    path('jobs/list/',JobList,name="jobs-list"),
    path('list/<int:key>',ApplicantList,name="applicant-list"),
    path('job/<int:key1>/studentresume/<int:key>/',StudentResumeView,name="student-resume-c"),
    path('select/<int:key1>/<int:key>/',SelectedStudent,name="student-select-c"),
    path('invite/<int:key1>/<int:key>/',Invitedstudents,name="student-invite-c"),
    path('reject/<int:key1>/<int:key>/',RejectedStudent,name="student-reject-c"),
    path('reject/revert/<int:key>/',RevertRejected,name="revert-reject-c"),
    path('hide/<int:key>',HideJob,name="hide-job"),
    path('applicant/',ApplicantHomeView,name="applicant-home-view"),
    path('invited/',InvitedHomeView,name="invited-home-view"),
    path('selected/',SelectedHomeView,name="selected-home-view"),
    path('companyprofile/',CompanyProfilePage,name="company-profile"),
    path('quiz/stats/<int:key>',TestStats,name="test-stats"),

]
