# from xml.dom.domreg import registered
# from multiprocessing import context
from django.shortcuts import render ,redirect , HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
# from django.contrib.auth.models import User
from accounts.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .forms import *

# from app.forms import MemberRegistrationForm
# Create your views here.



def adminsignup_view(request):
    form = AdminRegisterForm()
    if request.method=='POST':
        form=AdminRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            # groups = Group.objects.filter(name='ADMIN')
            # user.groups.add(*groups)

            return redirect('admin-login')
    return render(request,'accounts/admin_register.html',{'form':form})

def membersignup_view(request):
    form = MemberRegisterForm()
    context={'form':form}
    if request.method=='POST':
        form = MemberRegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            
            # my_student_group = Group.objects.get_or_create(name='MEMBER')
            # my_student_group[0].user_set.add(user)

            groups = Group.objects.filter(name='ADMIN')
            user.groups.add(*groups)
            return redirect('member-login')
        return HttpResponseRedirect('Jaa na Lovde')
    return render(request,'accounts/member_register.html',context)

def AdminLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, "Your username doesn't exists!")
            return HttpResponse("HEllo, You are not an user!")
            
        login(request, user ,backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            return redirect('afterlogin')
        else:
            # messages.error(request,"User does not exist.")
            return redirect('admin-login')

    return render(request, 'accounts/admin_login.html')





def MemberLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, "Your username doesn't exists!")
            return HttpResponse("HEllo")
            
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            return redirect('profile-form')
        else:
            # messages.error(request,"User does not exist.")
            return redirect('member-login')

    return render(request, 'accounts/member_login.html')


def LogoutUser(request):
    logout(request)
    return redirect ("home")


def jjj(request):
    return render(request , 'accounts/d.html')


# ---------------------------------- JWT Auth ---------------------------------------

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)


