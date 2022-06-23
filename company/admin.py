from django.contrib import admin
from .models import CompanyProfile,Job,Applicants,Selected,Rejected,InvitedStudent
# Register your models here.
admin.site.register(CompanyProfile)
admin.site.register(Job)
admin.site.register(Applicants)
admin.site.register(Selected)
admin.site.register(Rejected)
admin.site.register(InvitedStudent)