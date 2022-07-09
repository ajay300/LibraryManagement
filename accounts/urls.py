
from django.contrib import admin
from django.urls import path , include
from . import views
# from app import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView

from .views import MemberLogin, SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView

urlpatterns = [

    path('admin_signup/', views.adminsignup_view , name = 'admin-register'),
    path('member_signup/', views.membersignup_view , name = 'member-register'),



    # Since we have make the USer Custome Model so can skip this.
    # path('admin_login/', LoginView.as_view(template_name='accounts/admin_login.html' , next_page = 'afterlogin') , name ='admin-login'),
    # path('member_login/', LoginView.as_view(template_name='accounts/member_login.html' , next_page ='profile-form') , name = 'member-login'),

    path('admin_login/',views.AdminLogin , name = 'admin-login') ,
    path('member_login/',views.MemberLogin , name = 'member-login' ),

    
    
    
    # path('registration/',views.RegistrationView.as_view() , name='register'),
    path('logout/',views.LogoutUser , name = 'logout-user'),



    # --------------
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile_view/', UserProfileView.as_view(), name='profile-jwt'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

    
    
]


# 135387