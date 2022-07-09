
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home, name = 'home'),
    path('add-book/',views.BookView.as_view(),name ='add-book'),
    path('afterlogin/', views.afterlogin_view , name="afterlogin"),

    path('adminclick/', views.adminclick_view , name = 'admin-click'),
    path('memberclick/', views.memberclick_view , name = 'member-click'),
    
    

    path('book-list/',views.BookList.as_view() , name = 'book-list'),
    path('member-list/',views.MemberList , name = 'member-list'),

    path('issue-book/',views.Issue_bookView.as_view() , name = "issue-book"),
    path('profileform/',views.ProfileFormView.as_view() , name = 'profile-form'),

    path("view_books/", views.BookList.as_view(), name="view-books"),
    
    
    path("view_issued_book/", views.view_issued_book, name="view-issued-book"),
    path("member_issued_books/", views.member_issued_books, name="member_issued_books"),

    path("profile/<int:pk>/", views.ProfileView, name="profile"),
    # path("edit_profile/", views.edit_profile, name="edit_profile"),


    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
    path("delete_member/<int:pk>/", views.delete_member, name="delete_member"),


    
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


# 135387