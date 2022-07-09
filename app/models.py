# from distutils.command.upload import upload
from django.db import models
# from django.contrib.auth.models import User
# from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from datetime import datetime,timedelta
from .book_category import CATEGORY_CHOICE





class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=15 , choices=CATEGORY_CHOICE , default='education')

    def __str__(self):
        return str(self.title) + " ["+str(self.isbn)+']'

class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="profile_pic" ,blank=True)
    std = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    phone = models.IntegerField()
    branch = models.CharField(max_length=10 , blank=True)


def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, blank=True) 
    issued_date = models.DateField(auto_now=True)
    isbn = models.CharField(max_length=13)
    expiry_date = models.DateField(default=expiry)




