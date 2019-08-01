from rest_framework import serializers
from .models import  Messaging
from django.contrib.auth import authenticate , login
from rest_framework import exceptions
from django.contrib.auth.models import User



class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']





class Messagingserializer(serializers.ModelSerializer):

    class Meta:
        model = Messaging
        fields = ['sender' , 'recevier' , 'content' , 'subject' , 'creation_date' , 'readable']
