from django.urls import path
from .views import JobListManager, home_view,AddNoticeView,NoticeHomeView,NoticeEditView,DeleteNoticeView,HideNotice,VerifyStudent,VerifyResume,FinalVerify,SelectedStudentList,AppliedStudentList,JobListManager

urlpatterns=[
    path('<int:key>',home_view,name='mhome'),
    path('addnotice/',AddNoticeView.as_view(),name="add-notice"),
    path('notice/',NoticeHomeView.as_view(),name="notice-home"),
    path('notice/edit/<int:pk>',NoticeEditView.as_view(),name="notice-edit"),
    path('notice/delete/<int:pk>',DeleteNoticeView.as_view(),name="notice-delete"),
    path('notice/hide/<int:key>',HideNotice,name="notice-hide"),
    path('verify/',VerifyStudent,name="verify-student"),
    path('verify/Resume/<int:key>',VerifyResume,name="verify-resume"),
    path('verified/Resume/<int:key>',FinalVerify,name="verified-resume"),
    path('selected/',SelectedStudentList,name="selected-student"),
    path('applied/',AppliedStudentList,name="applied-student"),
    path('jobs/',JobListManager,name='jobs-list-m'),

]
