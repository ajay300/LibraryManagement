

from django.urls import path
from . import views

urlpatterns = [
    

    #-------- Book Api url
    path('bookview/',views.BookListcreate.as_view()),
    path('bookadd/<int:pk>/',views.BookRetrieveUpdate.as_view()),
    path('bookapiremove/<int:pk>',views.BookRetrieveDestroy.as_view()),

    #-------- Member APi url
    path('memberview/',views.BookListcreate.as_view()),
    path('memberadd/<int:pk>/',views.BookRetrieveUpdate.as_view()),
    path('memberapiremove/<int:pk>',views.BookRetrieveDestroy.as_view()),


    
] 


# 135387