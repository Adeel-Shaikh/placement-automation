from django.urls import path
from .views import UserRegisterView,LoginView,logout_view
urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('',LoginView,name='login'),
    path('logout/',logout_view,name="logout"),


]