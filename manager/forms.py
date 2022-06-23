from django import forms
from .models import Notice,changesNote

class NoticeForm(forms.ModelForm):
    class Meta:
        model=Notice
        fields=('user','college_name','topic','description','event_date','organized_by','students_eligible')
        widgets={
            'user': forms.TextInput(attrs={'value':' ','id':'user-notice-box','type':'hidden','class':'form-control'}),
            'college_name':forms.TextInput(attrs={'class':'form-control'}),
            'topic':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'event_date':forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'organized_by':forms.TextInput(attrs={'class':'form-control'}),
            'students_eligible':forms.Textarea(attrs={'rows':3,'class':'form-control','placeholder':"Enter Elgibilty Line By Line"}),

        }

class ChangesForm(forms.ModelForm):
    class Meta:
        model=changesNote

        fields=('student','note')
        widgets={
            'student': forms.TextInput(attrs={'value':' ','id':'student-box','type':'hidden','class':'form-control'}),
            'note':forms.Textarea(attrs={'class':'form-control'}),
        }
