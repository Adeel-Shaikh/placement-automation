from django import forms
from .models import Query, Reply
from company.models import CompanyProfile


class QueryForm(forms.ModelForm):

    class Meta:
        choice = CompanyProfile.objects.all().values_list('company_name', 'company_name')
        choice_list = [('general', 'general')]
        for item in choice:
            choice_list.append(item)
        model = Query
        fields = ('user', 'title', 'body', 'sub_forum')
        widgets = {
            'user': forms.TextInput(attrs={'value': ' ', 'id': 'user-box-forum', 'type': 'hidden', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"}),
            'sub_forum': forms.Select(choices=choice_list, attrs={'class': "form-control"}),
        }


class ReplyForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={
                           'value': ' ', 'id': 'user-box-forum', 'class': 'form-control', 'type': 'hidden'}))
    question = forms.CharField(widget=forms.TextInput(
        attrs={'value': ' ', 'id': 'q-box-forum', 'class': 'form-control', 'type': 'hidden'}))
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Reply to this Question!', 'class': 'form-control'}))
