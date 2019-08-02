from django.urls import path , include
from . import views
from Chat import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as aview

#urls using path for function.
urlpatterns = [
    path(r'', views.index),
    path(r'rest-auth/', include('rest_auth.urls')), #lib form django  login , logout and etc
     path('api-token-auth/', aview.obtain_auth_token), # lib form authentication
    path(r'Users/', views.user_list), #checking
    path(r'messaging/',views.get_message_by_id), #extract messaging by id
    path(r'unread/<int:user_id>/',views.unread_message_by_id), #extract messaging unread by id
    path(r'read/<int:message_id>/',views.read_message_by_id), #extract messaging(one) by id
    path(r'delete/<int:message_id>/',views.delete_message),   #delete message by id
    path(r'create/', views.create_message), #create message json format

]
urlpatterns=format_suffix_patterns(urlpatterns)
