from django.shortcuts import render,redirect
from .forms import  CustomUserCreationForm,CustomUserAuthenticationForm
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model

def LoginView(request):
	if request.method == "POST":
		form = CustomUserAuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			user = authenticate(request,email=email,password=password)
			User=get_user_model().objects.get(email=email)

			if user is not None:
				login(request,user)
				if User.user_type=='student':
					key=User.id
					return redirect("shome",key)
				elif User.user_type=='company':
					key=User.id
					return redirect("chome",key)
				elif User.user_type=='admin':
					key=User.id
					return redirect("mhome",key)
				else: 
					return redirect("home")

			else:
				return redirect("login")

		else:
			return redirect("login")
	else:
		form = CustomUserAuthenticationForm()

		return render(request,"registration/login.html",{"form":form}) 

def logout_view(request):
    logout(request)
    return redirect('home')

class  UserRegisterView(generic.CreateView):
    template_name='registration/register.html'
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')    


