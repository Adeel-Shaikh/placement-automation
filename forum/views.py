from django.shortcuts import render
from .models import Query,Reply
from company.models import CompanyProfile
from django.views.generic import CreateView,UpdateView
from .forms import QueryForm,ReplyForm
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def MainPage(request):
    queries=Query.objects.all().order_by('-date_posted')
    q_count=Query.objects.all().count
    my_questions=Query.objects.filter(user=request.user)
    cp=CompanyProfile.objects.all()
    r_count=Reply.objects.filter(user=request.user).count()
    context={
        'queries':queries,
        'my_questions':my_questions,
        'q_count':q_count,
        'cp':cp,
        'r_count':r_count,
    }
    return render(request,'forum/main.html',context)

def SubForum(request,company):
    queries=Query.objects.filter(sub_forum=company).order_by('-date_posted')
    q_all_count=Query.objects.all().count
    q_count=Query.objects.filter(sub_forum=company).count
    my_questions=Query.objects.filter(user=request.user,sub_forum=company)
    cp=CompanyProfile.objects.all()
    context={
        'queries':queries,
        'q_count':q_count,
        'company':company,
        'q_all_count':q_all_count,
        'my_questions':my_questions,
        'cp':cp,
    } 
    return render(request,'forum/sub_forum.html',context)

def DeleteReply(request,pk):
    r=Reply.objects.get(id=pk)
    q=r.question.id
    r.delete()
    return redirect('detail-query',q)

def QueryDetailView(request,pk):
    query=Query.objects.get(id=pk)
    cp=CompanyProfile.objects.all()
    replies=Reply.objects.filter(question=query)
    if request.user.user_type== "company":
        all_queries=Query.objects.filter(sub_forum=request.user.companyprofile)
    else:
        all_queries=False

    print(all_queries)
    if request.method == 'POST':
        form=ReplyForm(request.POST)
        body=request.POST['body']
        r=Reply(user=request.user,question=query,body=body)
        form=ReplyForm()
        r.save()
        
        return redirect("detail-query",pk)

    else:
        form=ReplyForm()
    context={
        'query':query,
        'replies':replies,
        'form':form,
        'cp':cp,
        'all_queries':all_queries,
    }
    
    return render(request,'forum/detail_query.html',context)

class AddQuery(CreateView):
    model=Query
    form_class=QueryForm
    template_name='forum/add_query.html'

    def get_success_url(self):
        return reverse('forum-main')

class EditQuery(UpdateView):
    model=Query
    form_class=QueryForm
    template_name='forum/edit_query.html'


    def get_success_url(self):
        print(self.kwargs.get('pk'))
        return reverse('detail-query',args=[self.kwargs.get('pk')])
