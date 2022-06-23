from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from django import forms
from .models import CustomUser

class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model=CustomUser
        fields=('email','password')
        

    def __init__(self,*args,**kwargs):
        super(CustomUserAuthenticationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'         
        self.fields['password'].widget.attrs['class']='form-control'         
      
      
    
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','first_name','last_name','user_type','password1','password2')

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['class']='form-control'             
        self.fields['first_name'].widget.attrs['class']='form-control'  
        self.fields['last_name'].widget.attrs['class']='form-control'  
        self.fields['user_type'].widget.attrs['class']='form-control'  
        self.fields['password1'].widget.attrs['class']='form-control'  
        self.fields['password2'].widget.attrs['class']='form-control'  
        



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)