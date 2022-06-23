from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

# Create your views here.
def home_view(request):
    return render(request,'home.html',{})


def back_home(request):
    User=get_user_model().objects.get(email=request.user)
    if User.user_type=='student':
        key=User.id
        return redirect("shome",key)
    elif User.user_type=='company':
        key=User.id
        return redirect("chome",key)
    elif User.user_type=='admin':
        key=User.id
        return redirect("mhome",key)
	