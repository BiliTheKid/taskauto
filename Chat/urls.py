from django.urls import path , include
from . import views
from Chat import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as aview
urlpatterns = [
    path(r'', views.index),
    #path('login/', views.login),
    path(r'rest-auth/', include('rest_auth.urls')),
     path('api-token-auth/', aview.obtain_auth_token),
    path(r'Users/', views.user_list),
    path(r'messaging/<int:user_id>/',views.get_message_by_id),
    path(r'unread/<int:user_id>/',views.unread_message_by_id),
    path(r'read/<int:message_id>/',views.read_message_by_id),
    path(r'delete/<int:message_id>/',views.delete_message),
    path(r'create/', views.create_message),

]
urlpatterns=format_suffix_patterns(urlpatterns)
