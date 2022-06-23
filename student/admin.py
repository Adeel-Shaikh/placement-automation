from django.contrib import admin
from .models import StudentResume,SkillList,ProjectList

# Register your models here.
admin.site.register(StudentResume)
admin.site.register(SkillList)
admin.site.register(ProjectList)