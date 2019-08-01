from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class User(models.Model):
    permission_classes = (IsAuthenticated)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    #user_id = models.IntegerField()
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

# def get_success_url(self):
#         return User.objects.filter(id=self.request.user.id)
def __str__(self):
        return self.username

class Messaging(models.Model):
    # permission_classes = (IsAuthenticated)
    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    #message_id = models.IntegerField()
    sender = models.ForeignKey('User',on_delete=models.CASCADE, related_name='sender')
    recevier = models.ForeignKey('User',on_delete=models.CASCADE, related_name='recevier')
    content = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    readable = models.CharField(max_length=10)
