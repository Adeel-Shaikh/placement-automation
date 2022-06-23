from django.urls import path
from .views import MainPage,AddQuery,QueryDetailView,SubForum,EditQuery,DeleteReply

urlpatterns=[
    path('',MainPage,name="forum-main"),
    path('<str:company>',SubForum,name='sub-forum'),
    path('addquery/',AddQuery.as_view(),name="add-query"),
    path('editquery/<int:pk>',EditQuery.as_view(),name="edit-query"),
    path('detail/<int:pk>',QueryDetailView,name="detail-query"),
    path('delete/<int:pk>',DeleteReply,name="delete-reply"),
]