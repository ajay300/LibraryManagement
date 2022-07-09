from django.shortcuts import render
from app.models import *
from api.serializers import *
from rest_framework.generics import  ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView

# Create your views here.





class BookListcreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class MemberListcreate(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class MemberRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

class MemberRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
