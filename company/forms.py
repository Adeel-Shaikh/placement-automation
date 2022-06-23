from django import forms
from .models import CompanyProfile,Job

class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model=CompanyProfile
        fields=('user','company_name','preview','about','website','service_provided','address','headquaters','type_of_company','founded_on','speciality')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'company-box','type':'hidden','class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'preview':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'about':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'service_provided':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'headquaters':forms.TextInput(attrs={'class':'form-control'}),
            'type_of_company':forms.Select(attrs={'class':'form-control'}),
            'founded_on':forms.NumberInput(attrs={'class':'form-control'}),
            'speciality':forms.TextInput(attrs={'class':'form-control'})
            
            
        }

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=('user','position','expected','salary','vacancy','desc','job_time','job_responsibilty')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'job-box','type':'hidden','class':'form-control'}),
            'position':forms.TextInput(attrs={'class':'form-control'}),
            'expected':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'salary':forms.NumberInput(attrs={'class':'form-control'}),
            'vacancy':forms.NumberInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'job_time':forms.NumberInput(attrs={'class':'form-control'}),
            'job_responsibilty':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
        }
