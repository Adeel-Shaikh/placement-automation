from django import forms
from .models import StudentResume,SkillList,ProjectList

class ResumeForm(forms.ModelForm):
    class Meta:
        model=StudentResume
        fields=('user','phone_no','email2','address','addmission_no','dob','gender','branch','college','ssc','ssc_college','hsc','hsc_college','diploma','diploma_college',
        'sem1','sem2','sem3','sem4','sem5','sem6','sem7','sem8','attendance','Backlogs','career_obj','linkden_url','github_url')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'user-box','type':'hidden','class':'form-control'}),
            'phone_no': forms.TextInput(attrs={'class':'form-control'}),
            'email2': forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'addmission_no':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
            'college':forms.TextInput(attrs={'class':'form-control'}),
            'ssc':forms.NumberInput(attrs={'class':'form-control'}),
            'ssc_college':forms.TextInput(attrs={'class':'form-control'}),
            'hsc':forms.NumberInput(attrs={'class':'form-control'}),
            'hsc_college':forms.TextInput(attrs={'class':'form-control'}),
            'diploma':forms.NumberInput(attrs={'class':'form-control'}),
            'diploma_college':forms.TextInput(attrs={'class':'form-control'}),
            'sem1':forms.NumberInput(attrs={'class':'form-control'}),
            'sem2':forms.NumberInput(attrs={'class':'form-control'}),
            'sem3':forms.NumberInput(attrs={'class':'form-control'}),
            'sem4':forms.NumberInput(attrs={'class':'form-control'}),
            'sem5':forms.NumberInput(attrs={'class':'form-control'}),
            'sem6':forms.NumberInput(attrs={'class':'form-control'}),
            'sem7':forms.NumberInput(attrs={'class':'form-control'}),
            'sem8':forms.NumberInput(attrs={'class':'form-control'}),
            'attendance':forms.NumberInput(attrs={'class':'form-control'}),
            'Backlogs':forms.NumberInput(attrs={'class':'form-control'}),
            'career_obj':forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'linkden_url':forms.URLInput(attrs={'class':'form-control'}),
            'github_url':forms.URLInput(attrs={'class':'form-control'}),



        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model=ProjectList
        fields=('user','project_title','project_description','semester')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'user-box-project','type':'hidden','class':'form-control'}),
            'project_title': forms.TextInput(attrs={'class':'form-control'}),
            'project_description': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'semester': forms.Select(attrs={'class':'form-control'}),
        }

class SkillForm(forms.ModelForm):

    class Meta:
        model=SkillList
        fields=('user','skill_name','skill_type','skill_level')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'user-box-skill','type':'hidden','class':'form-control'}),
            'skill_name': forms.TextInput(attrs={'class':'form-control'}),
            'skill_type': forms.TextInput(attrs={'class':'form-control'}),
            'skill_level': forms.Select(attrs={'class':'form-control'}),
        }
