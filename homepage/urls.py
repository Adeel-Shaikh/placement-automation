from django.urls import path
from .views import home_view,back_home

urlpatterns=[
    path('',home_view,name='home'),
    path('home/view/',back_home,name='back-home'),
]