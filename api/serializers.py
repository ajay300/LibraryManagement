from rest_framework import serializers
from app.models import *







class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user','first_name','last_name','std','roll_no','phone','branch']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','isbn','category']
    