from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.parsers import JSONParser
from .models import User ,Messaging
from .serializers import Userserializer , Messagingserializer
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.response import Response




#Index page for task massage
@api_view(['GET', 'POST'])
def index(request):
    return HttpResponse("<h1>Messaging-system Task</h1>")




@api_view(['GET', 'POST'])
def user_list(request):
    """
    Api request for all users in the system, check.
    Extract Object from db get call / post create one.
    """
    if request.method == 'GET':
        current_user = request.user
        print(request.user.id)
        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def get_message_by_id(request):
    """
        Get request for all messages by user id
    """
    if request.method == 'GET':
        user_id = request._user.id
        messaging_sender = list(Messaging.objects.filter(sender=user_id))
        messaging_reciver = list(Messaging.objects.filter(recevier=user_id))
        messaging = messaging_sender + messaging_reciver
        serializer = Messagingserializer(messaging, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def unread_message_by_id(request,user_id):
    """
         Get request for all unread messages by user id
         using object.filter Q.
         """
    if request.method == 'GET':
        messaging_sender = list(Messaging.objects.filter(Q(sender=user_id) &Q(readable='false')))
        messaging_reciver = list(Messaging.objects.filter(Q(recevier=user_id) & Q(readable= 'false')))
        messaging = set(messaging_sender + messaging_reciver)
        serializer = Messagingserializer(messaging, many=True)
        structure = serializer.data
        return Response(structure)


@api_view(['GET', 'POST'])
def read_message_by_id(request,message_id):
    """
      Get request messages by message id
      using object.filter Q.
      """
    if request.method == 'GET':
        messaging = Messaging.objects.filter(message_id=message_id)
        serializer = Messagingserializer(messaging, many=True)
        return Response(serializer.data)



@api_view(['GET', 'POST','DELETE'])
def delete_message(request,message_id):
    """
       Delete request for  messages by message id

       """
    if request.method == 'DELETE':
        messaging = Messaging.objects.filter(message_id=message_id)
        serializer = Messagingserializer(messaging, many=True)
        structure = serializer.data
        if len(structure) == 0:
            return HttpResponse({'error: The message id doesnt exits'}, status=204)
        else:
            check = structure[0]['message_id']
            if check == message_id:
                messaging.delete()
                return HttpResponse({'The message deleted'},status=200)


@csrf_exempt
@api_view(['POST','GET'])
@permission_classes((AllowAny,))
def create_message(request):
    """
        create message
        """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Messagingserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
