# from attr import fields
from django import forms
from .models import Book, IssuedBook

from .models import Member
# from django.contrib.auth.models import User
# from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

        exclude = ['user']

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control mt-2'
            }),
            'author':forms.TextInput(attrs={
                'class':'form-control mt-2'
            }),
            'isbn':forms.TextInput(attrs={
                'class':'form-control mt-2'
            }),
            # 'category':forms.TextInput(attrs={
            #     'class':'form-control mt-2'
            # }),
            
            
        }

class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = '__all__'

# class MemberRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','email','password']

#         widgets = {
#             'username':forms.TextInput(attrs={
#                 'class':'form-control mt-2'
#             }),
#             'email':forms.TextInput(attrs={
#                 'class':'form-control mt-2'
#             }),
#             'password':forms.PasswordInput(attrs={
#                 'class':'form-control mt-2'
#             }),
            
            
#         }

        


class MemberProfile(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name','last_name','profile_pic','std','roll_no','phone','branch']

