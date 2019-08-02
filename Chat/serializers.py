from rest_framework import serializers
from .models import  Messaging
from django.contrib.auth.models import User


'''''
Serializers allow complex data such as querysets and model 
instances to be converted to native Python datatypes that can 
then be easily rendered...
https://www.django-rest-framework.org/api-guide/serializers/
'''''

#User Serializers
class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','password']




#Messages Serializers
class Messagingserializer(serializers.ModelSerializer):

    class Meta:
        model = Messaging
        fields = ['sender' , 'recevier' , 'content' , 'subject' , 'creation_date' , 'readable']
